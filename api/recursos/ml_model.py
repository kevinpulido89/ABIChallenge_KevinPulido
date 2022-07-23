import re
import pickle
from nltk.stem import WordNetLemmatizer
from dataclasses import dataclass
from .data_structure import Tuits, RespuestaModelo

lemmatizer = WordNetLemmatizer()

@dataclass
class ModelPipeline:

    loaded_model = pickle.load(open('./recursos/models/pipeline.pickle', 'rb'))

    pred_to_label = {0: 'Negative', 1: 'Positive'}

    emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad',
              ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
              ':-@': 'shocked', ':@': 'shocked', ':-$': 'confused', ':\\': 'annoyed',
              ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
              '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
              '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink',
              ';-)': 'wink', 'O:-)': 'angel', 'O*-)': 'angel', '(:-D': 'gossip', '=^.^=': 'cat'}

    stopwords = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
                'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before',
                'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do',
                'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
                'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
                'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
                'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
                'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once',
                'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'own', 're',
                's', 'same', 'she', "shes", 'should', "shouldve", 'so', 'some', 'such',
                't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
                'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
                'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
                'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
                'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre",
                "youve", 'your', 'yours', 'yourself', 'yourselves']

    def predict_pipeline(self, tweet: list[str]) -> RespuestaModelo:
        """Pipeline que a partir del modelo cargado procesa los Tuits y genera el resultado en una formato útil para la API

        Args:
            tweet (Tuits): lista con textos de tuits a predecir

        Returns:
            RespuestaModelo: lista de predicciones de tipo 'RespuestaModelo'. Empaqueta toda las respuestas en una lista válida para la API
        """

        return self.predict(model=self.loaded_model, text=tweet)


    def predict(self, model, text: list[str]) -> list:
        """Función en donde se genera la predicción en sí. A partir del modelo usa se procesa la lista de textos.

        Args:
            model (sklearn.pipeline.Pipeline): Modelo de clasificación de texto.
            text (list[str]): lista de textos a clasificar con el modelo pre-entrenado

        Returns:
            RespuestaModelo: lista de predicciones de tipo 'RespuestaModelo'. Una predicción por tuit con información del texto original, predicción (1/0) y etiqueta (Positive/Negative)
        """
        preprocessed_text = self.preprocess(text)
        predictions = model.predict(preprocessed_text)

        data = []
        for t, pred in zip(text, predictions):
            data.append({"tweet": t, "pred": int(pred), "label": self.pred_to_label[pred]})
        
        return data

    def preprocess(self, textdata:list[str]) -> list[str]:
        """Función de limpieza, preprocesamiento de cada texto de la lista. Remueve patrones, URLs, USERNAMES, stopwords y emojis.

        Args:
            textdata (list): lista de textos RAW.
        Returns:
            list: lista de textos preprocesados a clasificar con el modelo pre-entrenado,
        """
        processed_texts = []

        # Definir patrones ReGex.
        url_pattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
        user_pattern = '@[^\s]+'
        alpha_pattern = "[^a-zA-Z0-9]"
        sequence_pattern = r"(.)\1\1+"
        seq_replace_pattern = r"\1\1"

        # iterar y preprocesar cada tuit
        for tweet in textdata:
            tweet = tweet.lower()

            # Replace all URls with 'URL'
            tweet = re.sub(url_pattern, ' URL', tweet)
            
            # Replace all emojis.
            for emoji in self.emojis.keys():
                tweet = tweet.replace(emoji, "EMOJI" + self.emojis[emoji])
            
            # Replace @USERNAME to 'USER'.
            tweet = re.sub(user_pattern, ' USER', tweet)
            
            # Replace all non alphabets.
            tweet = re.sub(alpha_pattern, " ", tweet)
            
            # Replace 3 or more consecutive letters by 2 letter.
            tweet = re.sub(sequence_pattern, seq_replace_pattern, tweet)

            preprocessed_words = []
            for word in tweet.split():
                # Check if the word is a stopword.
                if len(word) > 1 and word not in self.stopwords:
                    # Lemmatizing the word.
                    word = lemmatizer.lemmatize(word)
                    preprocessed_words.append(word)

            processed_texts.append(' '.join(preprocessed_words))

        return processed_texts