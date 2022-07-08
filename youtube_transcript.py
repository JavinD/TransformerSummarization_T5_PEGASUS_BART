from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import csv

def generate_transcript(id):
    transcript = {"text": "-"}
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id, cookies="Project_Skripsi/cookies.txt")
    except Exception:
        pass
    
    script = ""

    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
        
    return script, len(script.split())

def parseCSV(path):
    
    columns = ["title", "channelTitle","videoId", "publishedDate"]
    df = pd.read_csv(path, usecols=columns)
    
    return df

def getTranscripts(df):
    count=0
    df_script=[]
    df_count=[]
    for id in df['videoId']:
        try:
            transcript, word_count = generate_transcript(id)
        except Exception:
            count-=1
            print (count-2)
            transcript="-"
        df_script.append(transcript)
        df_count.append(word_count)
        count+=1
        

    df['transcript'] = df_script
    df['wordCount'] = df_count

    return df


        
def main():
    path = "Project_Skripsi\Dataset\CNBC_Television.csv"
    out_path = "Project_Skripsi\Dataset\subCNBC_new.csv"
    # srt, no_of_words = generate_transcript(id) 
    df = parseCSV(path)
    
    
    df = getTranscripts(df)

    
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    
    main()