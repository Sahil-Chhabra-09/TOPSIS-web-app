from topsisGod import topsis
from topsisGod import rerank
import streamlit as st
import pandas as pd
import re



def main():
    st.title("TOPSIS(MCDM) Web App")
    st.text("TOPSIS is a method for Multiple Criteria Decision Making, this app allows it to be accessed easily")
    file_upload = st.file_uploader('Upload csv file containing only characteristics and not names of objects to be ranked')
    if file_upload is not None:
        df = pd.read_csv(file_upload)
        df = pd.get_dummies(df)
        st.header("Top 5 values of uploaded data:")
        st.write(df.head(10))
        st.markdown("""---""")
        st.write("Enter weights of each characteristics seperated by ' , '")
        weights = st.text_input("No. of weights should be " + str(len(df.columns)))
        weights = weights.split(',')
        if len(weights) != len(df.columns):
            st.write("No. of weights do not match columns")
        else:
            weights = [float(x) for x in weights]
            st.markdown("""---""")
            st.write("Enter impacts of each characteristics as : (+, -), seperated by ','")
            impacts = st.text_input("No. of impacts should be " + str(len(df.columns)))
            impacts = re.sub(" ","", impacts)
            impacts = impacts.split(',')
            if len(weights) != len(df.columns):
                st.write("No. of impacts do not match columns")
            else:
                score = topsis(df, weights, impacts)
                show = st.checkbox("Show ranked dataset:")
                if show:
                    st.write(rerank(df, score,inplace=False))
                st.write("Scores of each object are:")
                st.success(score)
                finalrank = []
                rankings = rerank(df, score, inplace=False).index.tolist()
                for x in rankings:
                    finalrank.append(x+1)
                st.write("Final Ranks are: ")
                st.success(finalrank)
            
        

if __name__ == '__main__':
    main()