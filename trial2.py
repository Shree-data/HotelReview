# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:49:53 2023

@author: Shriprada
"""

import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


clear = st.button("CLEAR")

def main():
    
    st.title("HOTEL REVIEW - SENTIMENT ANALYSIS")
    st.subheader("Sentiment Analysis on the review")
    review = st.text_area("Enter the Review", "Type Here")
    
    def hotel(text, op):
        if op == 'Sent Tokenize':
            sent_tokenized = nltk.sent_tokenize(text)
            result = {"result": sent_tokenized}
            result = {key:value for key, value in result.items()}
            res = result['result']
            return res
        if op == 'Word Tokenize':
            word_tokenized = nltk.word_tokenize(text)
            result = {"result": word_tokenized}
            result = {key:value for key, value in result.items()}
            res = result['result']
            return res
        if op == 'Lemmatize':
            wnl = WordNetLemmatizer()
            words = nltk.word_tokenize(text)
            clean_data = []
            for words in words:
                if not words in stopwords.words('english'):
                    clean_data.append(words)
            lemma = [wnl.lemmatize(word) for word in clean_data]
            result = {"result":"\n".join(lemma,)}
            result = {key: value for key, value in result.items()}
            res = result['result']
            return res
        if op == 'Sentiment':
            blob = TextBlob(review)      
            if blob.sentiment.polarity > 0 :
                st.write('Positive')
            elif blob.sentiment.polarity == 0 :
                st.write("Neutral")
            else:
                st.write("negative")    
            sentiment = blob.sentiment
            result = {"result": sentiment}
            result = {key:value for key, value in result.items()}
            res = result['result']
            st.success(result)
            return res
        
    
    
    
    choice = st.selectbox("SELECT NLP FUNCTION", ('Lemmatize',
                                    'Sent Tokenize','Word Tokenize',
                                    'Sentiment'))
    

    if choice == 'Lemmatize' and len(review) > 0:
        output = hotel(review,'Lemmatize')
        st.text_area("Output", output, height=200)
    
    elif choice == 'Sent Tokenize' and len(review) > 0:
        output = hotel(review,'Sent Tokenize')
        st.text_area("Output",output,height=200)
   
    elif choice == 'Word Tokenize' and len(review) > 0:
        output = hotel(review,'Word Tokenize')
        st.text_area("Output",output,height=200)
        
    elif choice == 'Sentiment' and len(review) > 0:
        output = hotel(review,'Sentiment')
        st.text_area("Output",output,height=200)
    
            
            
if __name__ == '__main__':
    main()
    
