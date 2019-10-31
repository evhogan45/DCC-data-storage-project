import pandas as pd
import docx

def searcher(field, condition):
  frame2 = pd.read_csv(r"X:\DCC Investigations\DCC Database\analysis\report data.csv")
  frame2 = frame2.drop(labels = 'Unnamed: 0', axis = 1)
  return(frame2[frame2[field].str.contains(condition, na = False)]) 

def dubSearcherInc(field1, condition1, field2, condition2):
  frame2 = pd.read_csv(r"X:\DCC Investigations\DCC Database\analysis\report data.csv")
  frame2 = frame2.drop(labels = 'Unnamed: 0', axis = 1)
  oneFrame = (frame2[frame2[field1].str.contains(condition1, na = False)])
  otherFrame = (frame2[frame2[field2].str.contains(condition2, na = False)])
  frame3 = (pd.concat([oneFrame, otherFrame]))
  return(frame3.drop_duplicates(keep = "last"))

def dubSearcherExc(field1, condition1, field2, condition2):
  frame2 = pd.read_csv(r"X:\DCC Investigations\DCC Database\analysis\report data.csv")
  frame2 = frame2.drop(labels = 'Unnamed: 0', axis = 1)
  oneFrame = (frame2[frame2[field1].str.contains(condition1, na = False)])
  otherFrame = (oneFrame[oneFrame[field2].str.contains(condition2, na = False)])
  return(otherFrame)

def names(name): 
  frame2 = pd.read_csv(r"X:\DCC Investigations\DCC Database\analysis\report data.csv")
  frame2 = frame2.drop(labels = 'Unnamed: 0', axis = 1)
  oneFrame = (frame2[frame2['names'].str.contains(name, na = False)])
  twoFrame = (frame2[frame2['reference'].str.contains(name, na = False)])
  threeFrame = (frame2[frame2['summary'].str.contains(name, na = False)])
  master = pd.concat([oneFrame, twoFrame, threeFrame])
  return(master.drop_duplicates())

def inClemis(name):
  frame2 = pd.read_csv(r"X:\DCC Investigations\DCC Database\analysis\CLEMIS master.csv", encoding = "ISO-8859-1")
  oneFrame = (frame2[frame2['Name'].str.contains(name, na = False)])
  twoFrame = (frame2[frame2['Ofense'].str.contains(name, na = False)])
  master = pd.concat([oneFrame, twoFrame])
  master.drop_duplicates()
  return(master.drop(labels = 'Unnamed: 0', axis = 1))
