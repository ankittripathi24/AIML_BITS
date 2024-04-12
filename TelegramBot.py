import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackContext
import joblib
import pickle
import string
import re


TOKEN="7168888956:AAE61RjOc5thfDI0EwnNjzJJT-WhhVsjX-Y"
model = joblib.load("model.pkl")
tfidf_vectorizer = joblib.load("vectorizer.pkl")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am Analytical Bot! I can help you with your Tweet's Sentimant Analysis.")

def handle_response(text: str) -> str:
    if text == "Hello":
        return "Hi there!"
    else:
        return "I don't understand you"
    
def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = handle_response(update.message.text)
    update.message.reply_text(response)

with open('final_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

def preProcessTweet(tweet):
    # Convert the tweet to lowercase
    tweet = tweet.lower()
    # Remove URLs
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    # Remove user @ references and '#' from tweet
    spec_chars = ["!",'"',"#","%","&","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]
    for sc in spec_chars:
        tweet = tweet.replace(sc, '')
    # Remove punctuations
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    
    return tweet

async def handle_responses(update: Update, context: CallbackContext) -> int:
    tweet_text = update.message.text

    preprocessed_tweet = preProcessTweet(tweet_text)

    # Convert the preprocessed tweet text into TF-IDF features
    tfidf_features = tfidf_vectorizer.transform([preprocessed_tweet])
    
    # Make predictions using the loaded model
    prediction = loaded_model.predict(tfidf_features)
    
    prediction = str(prediction)
    print(prediction)
    

    if isinstance(tweet_text, str) and not tweet_text.isalnum():
        await update.message.reply_text(prediction)
    else:
        await update.message.reply_text("I don't understand you")


    return "Hello there!"

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT, handle_responses))
    
    application.run_polling()