#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2016 Joshua Przyborowski - https://github.com/JoshuaPrzyborowski

    $FileInfo: pydice.py - Last Update: 10/12/2016 Ver. 0.2.5 RC 1 - Author: joshuatp $
'''

from __future__ import division, absolute_import, print_function;
from collections import OrderedDict;
import re, random;
try:
 import xml.etree.cElementTree as cElementTree;
except ImportError:
 import xml.etree.ElementTree as cElementTree;

__program_name__ = "PyDice-Roll";
__project__ = __program_name__;
__project_url__ = "https://github.com/JoshuaPrzyborowski/PyDice";
__version_info__ = (0, 2, 5, "RC 1", 1);
__version_date_info__ = (2016, 10, 12, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
if(__version_info__[4]!=None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4]==None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def GetMinValues(DiceList, DiceNum=5):
 if type(DiceList) is not list:
  return False;
 if type(DiceNum) is not int:
  DiceNum = 5;
 MinValList = [];
 UsedVals = [];
 MinValDict = OrderedDict();
 ilist = 1;
 ixlist = DiceNum;
 while(ilist<=ixlist):
  subilist = 0;
  subixlist = len(DiceList);
  curminval = float('inf');
  curvalpos = 0;
  while(subilist<subixlist):
   if(DiceList[subilist]<curminval and subilist not in UsedVals):
    curminval = DiceList[subilist];
    curvalpos = subilist + 1;
   subilist = subilist + 1;
  UsedVals.append(curvalpos - 1);
  MinValDict.update({curvalpos: curminval});
  ilist = ilist + 1;
 MinValDict = OrderedDict(sorted(MinValDict.items()));
 for key, value in MinValDict.items():
  MinValList.append(value);
 return MinValList;

def GetMaxValues(DiceList, DiceNum=5):
 if type(DiceList) is not list:
  return False;
 if type(DiceNum) is not int:
  DiceNum = 5;
 MaxValList = [];
 UsedVals = [];
 MaxValDict = OrderedDict();
 ilist = 1;
 ixlist = DiceNum;
 while(ilist<=ixlist):
  subilist = 0;
  subixlist = len(DiceList);
  curmaxval = 0;
  curvalpos = 0;
  while(subilist<subixlist):
   if(DiceList[subilist]>curmaxval and subilist not in UsedVals):
    curmaxval = DiceList[subilist];
    curvalpos = subilist + 1;
   subilist = subilist + 1;
  UsedVals.append(curvalpos - 1);
  MaxValDict.update({curvalpos: curmaxval});
  ilist = ilist + 1;
 MaxValDict = OrderedDict(sorted(MaxValDict.items()));
 for key, value in MaxValDict.items():
  MaxValList.append(value);
 return MaxValList;

def RandomDiceRoll(MinNum=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 if(len(re.findall("^([\-]?[0-9]+)$", str(MinNum)))<1):
  MinNum = 1;
 try:
  MinNum = int(MinNum);
 except ValueError:
  return [False];
 if(len(re.findall("^([\-]?[0-9]+)$", str(MaxNum)))<1):
  MaxNum = 6;
 try:
  MaxNum = int(MaxNum);
 except ValueError:
  return [False];
 if(len(re.findall("^([\-]?[1-4]+)$", str(RandType)))<1):
  RandType = 1;
 try:
  RandType = int(RandType)
 except ValueError:
  RandType = 1;
 if(MinNum>MaxNum):
  TmpMinNum = MaxNum;
  TmpMaxNum = MinNum;
  MaxNum = TmpMaxNum;
  MinNum = TmpMinNum;
 RandType = int(RandType);
 if(RandType<1):
  RandType = 1;
 if(RandType>4):
  RandType = 4;
 if(RandType==1):
  DiceRollValue = random.randint(MinNum, MaxNum);
 if(RandType==2):
  randtype = random.WichmannHill(RandSeed);
  DiceRollValue = randtype.randint(MinNum, MaxNum);
 if(RandType==3):
  randtype = random.SystemRandom(RandSeed);
  DiceRollValue = randtype.randint(MinNum, MaxNum);
 if(RandType==4):
  DiceRollValue = random.randrange(MinNum, MaxNum + 1);
 return [DiceRollValue];

def RandomDieRoll(MinNum=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 return RandomDiceRoll(MinNum, MaxNum, RandType, RandSeed);

def RandomDiceRollAlt(MaxNum=6, RandType=1, RandSeed=random.seed()):
 if(MaxNum>0):
  return [RandomDiceRoll(1, MaxNum, RandType, RandSeed)[0]];
 if(MaxNum<0):
  return [RandomDiceRoll(MaxNum, -1, RandType, RandSeed)[0]];
 if(MaxNum==0):
  return [RandomDiceRoll(MaxNum, 1, RandType, RandSeed)[0]];

def RandomDieRollAlt(MaxNum=6, RandType=1, RandSeed=random.seed()):
 return RandomDiceRollAlt(MaxNum, RandType, RandSeed);

def RandomRollMultiDice(MinNum=[1], MaxNum=[6], RandType=1, RandSeed=random.seed()):
 if not isinstance(MinNum, list):
  MinNum = [MinNum];
 if not isinstance(MaxNum, list):
  MaxNum = [MaxNum];
 CountMinNum = len(MinNum);
 CountMaxNum = len(MaxNum);
 if(CountMinNum>=CountMaxNum):
  NumOfDice = CountMinNum;
 if(CountMinNum<CountMaxNum):
  NumOfDice = CountMaxNum;
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  DiceRolls.append(RandomDiceRoll(MinNum[CountNumOfDice], MaxNum[CountNumOfDice], RandType, RandSeed)[0]);
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDie(MinNum=[1], MaxNum=[6], RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDice(MinNum, MaxNum, RandType, RandSeed);

def RandomRollMultiDiceByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 dieminv = [];
 diemaxv = [];
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   diemin = "";
   if('min' in child.attrib):
    diemin = str(child.attrib['min']);
   else:
    diemin = "1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemin))<1):
    diemin = "1";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dieminv.append(diemin);
   diemaxv.append(diemax);
 return RandomRollMultiDice(dieminv, diemaxv, RandType, RandSeed);

def RandomRollMultiDieByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceAlt(MaxNum=[6], RandType=1, RandSeed=random.seed()):
 if not isinstance(MaxNum, list):
  MaxNum = [MaxNum];
 NumOfDice = len(MaxNum);
 CountNumOfDice = 0;
 DiceRollsMin = [];
 DiceRollsMax = [];
 while(CountNumOfDice<NumOfDice):
  if(MaxNum[CountNumOfDice]>0):
   DiceRollsMin.append(1);
   DiceRollsMax.append(MaxNum[CountNumOfDice]);
  if(MaxNum[CountNumOfDice]<0):
   DiceRollsMin.append(MaxNum[CountNumOfDice]);
   DiceRollsMax.append(-1);
  if(MaxNum[CountNumOfDice]==0):
   DiceRollsMin.append(MaxNum[CountNumOfDice]);
   DiceRollsMax.append(1);
  CountNumOfDice = CountNumOfDice + 1;
 DiceRolls = RandomRollMultiDice(DiceRollsMin, DiceRollsMax, RandType, RandSeed);
 return DiceRolls;

def RandomRollMultiDieAlt(MaxNum=[6], RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceAlt(MaxNum, RandType, RandSeed);

def RandomRollMultiDiceAltByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diemaxv = [];
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   diemaxv.append(diemax);
 return RandomRollMultiDiceAlt(diemaxv, RandType, RandSeed);

def RandomRollMultiDieAltByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceAltByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiSameDice(NumOfDice=1, MinNum=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 CountNumOfDice = 0;
 DiceRollsMin = [];
 DiceRollsMax = [];
 while(CountNumOfDice<NumOfDice):
  DiceRollsMin.append(MinNum);
  DiceRollsMax.append(MaxNum);
  CountNumOfDice = CountNumOfDice + 1;
 DiceRolls = RandomRollMultiDice(DiceRollsMin, DiceRollsMax, RandType, RandSeed);
 return DiceRolls;

def RandomRollMultiSameDie(NumOfDie=1, MinNum=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiSameDice(NumOfDie, MinNum, MaxNum, RandType, RandSeed);

def RandomRollMultiSameDiceAlt(NumOfDice=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 CountNumOfDice = 0;
 DiceRollsMin = [];
 DiceRollsMax = [];
 while(CountNumOfDice<NumOfDice):
  if(MaxNum>0):
   DiceRollsMin.append(1);
   DiceRollsMax.append(MaxNum);
  if(MaxNum<0):
   DiceRollsMin.append(MaxNum);
   DiceRollsMax.append(-1);
  if(MaxNum==0):
   DiceRollsMin.append(MaxNum);
   DiceRollsMax.append(1);
  CountNumOfDice = CountNumOfDice + 1;
 DiceRolls = RandomRollMultiDice(DiceRollsMin, DiceRollsMax, RandType, RandSeed);
 return DiceRolls;

def RandomRollMultiSameDieAlt(NumOfDie=1, MaxNum=6, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiSameDiceAlt(NumOfDie, MaxNum, RandType, RandSeed);

def RandomRollDiceByPosition(DiceStr="0,0,0,0,0,1", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  CurDiceNum = CountNumOfDice + 1;
  if(int(DiceStrList[CountNumOfDice])>0):
   DiceRolls = DiceRolls + RandomRollMultiSameDiceAlt(int(DiceStrList[CountNumOfDice]), CurDiceNum, RandType, RandSeed);
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollDieByPosition(DieStr="0,0,0,0,0,1", RandType=1, RandSeed=random.seed()):
 return RandomRollDiceByPosition(DieStr, RandType, RandSeed);

def RandomRollDiceByString(DiceStr="d6", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("c", "d2", DiceStr);
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetDiceRoll = int(re.findall("d([0-9]+)", DiceStrList[CountNumOfDice])[0]);
  DiceRolls = DiceRolls + RandomDiceRollAlt(GetDiceRoll, RandType, RandSeed);
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollDieByString(DieStr="d6", RandType=1, RandSeed=random.seed()):
 return RandomRollDiceByString(DieStr, RandType, RandSeed);

def RandomRollDiceByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   diestr = "d"+diemax;
 return RandomRollDiceByString(diestr, RandType, RandSeed);

def RandomRollDieByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollDiceByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceByString(DiceStr="1d6", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("([0-9]*)c", "\\1d2", DiceStr);
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetPreDiceRoll = re.findall("([0-9]*)d([0-9]+)([l|h]?[0-9]*)", DiceStrList[CountNumOfDice])[0];
  if(GetPreDiceRoll[1]==""):
   GetDiceRoll = 1;
  else:
   GetDiceRoll = int(GetPreDiceRoll[1]);
  GetNumDice = int(GetPreDiceRoll[0]);
  GetDiceAVGList = "";
  if(not GetPreDiceRoll[2]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[2]))>0):
    GetDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[2])[0];
   else:
    GetPreDiceRoll[2] = "";
  GetPreDiceRollList = [];
  if(GetNumDice>0):
   GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDiceAlt(GetNumDice, GetDiceRoll, RandType, RandSeed);
  if(GetPreDiceRoll[2]==""):
   GetDiceRollList = GetPreDiceRollList;
  else:
   if(int(GetDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetDiceAVGList[0]=="l"):
    GetDiceRollList = GetMinValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   if(GetDiceAVGList[0]=="h"):
    GetDiceRollList = GetMaxValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   DiceRolls = DiceRolls + GetDiceRollList;
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDieByString(DieStr="1d6", RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceByString(DieStr, RandType, RandSeed);

def RandomRollMultiDiceByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"d"+diemax;
  if(child.tag=="coin"):
   if(diestr!=""):
    diestr = diestr+",";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"c";
 return RandomRollMultiDiceByString(diestr, RandType, RandSeed);

def RandomRollMultiDieByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceByStringAlt(DiceStr="d6:1", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("c([\:]?[0-9])", "d2\\1", DiceStr);
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetPreDiceRoll = re.findall("d([0-9]+)([\:]?[0-9]*)([l|h]?[0-9]*)", DiceStrList[CountNumOfDice])[0];
  GetDiceRoll = int(GetPreDiceRoll[0]);
  GetPreNumDice = GetPreDiceRoll[1].replace(":", "");
  if(GetPreNumDice==""):
   GetNumDice = 1;
  else:
   GetNumDice = int(GetPreNumDice);
  GetDiceAVGList = "";
  if(not GetPreDiceRoll[2]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[2]))>0):
    GetDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[2])[0];
   else:
    GetPreDiceRoll[2] = "";
  GetPreDiceRollList = [];
  if(GetNumDice>0):
   GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDiceAlt(GetNumDice, GetDiceRoll, RandType, RandSeed);
  if(GetPreDiceRoll[2]==""):
   GetDiceRollList = GetPreDiceRollList;
  else:
   if(int(GetDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetDiceAVGList[0]=="l"):
    GetDiceRollList = GetMinValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   if(GetDiceAVGList[0]=="h"):
    GetDiceRollList = GetMaxValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   DiceRolls = DiceRolls + GetDiceRollList;
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDieByStringAlt(DieStr="d6:1", RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceByStringAlt(DieStr, RandType, RandSeed);

def RandomRollMultiDiceByXMLAlt(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+"d"+diemax+":"+dienum;
 return RandomRollMultiDiceByStringAlt(diestr, RandType, RandSeed);

def RandomRollMultiDieByXMLAlt(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceByXMLAlt(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceMinMaxByString(DiceStr="1d1:6", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("([0-9]*)c", "\\1d1:2", DiceStr);
 DiceStr = re.sub("([0-9]*)u([0-9]+)([l|h]?[0-9]*)", "\\1d-\\2:\\2\\3", DiceStr);
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetPreDiceRoll = re.findall("([0-9]*)d([\-]?[0-9]+)([\:]?[\-]?[0-9]*)([l|h]?[0-9]*)", DiceStrList[CountNumOfDice])[0];
  if(GetPreDiceRoll[1]==""):
   GetMinDiceRoll = 1;
  else:
   GetMinDiceRoll = int(GetPreDiceRoll[1]);
  GetPreMaxDiceRoll = GetPreDiceRoll[2].replace(":", "");
  if(GetPreMaxDiceRoll==""):
   GetMaxDiceRoll = "";
  else:
   GetMaxDiceRoll = int(GetPreMaxDiceRoll);
  GetNumDice = int(GetPreDiceRoll[0]);
  GetDiceAVGList = "";
  if(not GetPreDiceRoll[3]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[3]))>0):
    GetDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[3])[0];
   else:
    GetPreDiceRoll[3] = "";
  GetPreDiceRollList = [];
  if(GetNumDice>0):
   if(GetMaxDiceRoll==""):
    GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDiceAlt(GetNumDice, GetMinDiceRoll, RandType, RandSeed);
   else:
    GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDice(GetNumDice, GetMinDiceRoll, GetMaxDiceRoll, RandType, RandSeed);
  if(GetPreDiceRoll[3]==""):
   GetDiceRollList = GetPreDiceRollList;
  else:
   if(int(GetDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetDiceAVGList[0]=="l"):
    GetDiceRollList = GetMinValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   if(GetDiceAVGList[0]=="h"):
    GetDiceRollList = GetMaxValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
  DiceRolls = DiceRolls + GetDiceRollList;
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDieMinMaxByString(DieStr="1d1:6", RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceMinMaxByString(DieStr, RandType, RandSeed);

def RandomRollMultiDiceMinMaxByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   diemin = "";
   if('min' in child.attrib):
    diemin = str(child.attrib['min']);
   else:
    diemin = "1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemin))<1):
    diemin = "1";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"d"+diemin+":"+diemax;
  if(child.tag=="fudge"):
   if(diestr!=""):
    diestr = diestr+",";
   diemin = "";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
    diemin = "-"+str(child.attrib['max']);
   else:
    diemax = "1";
    diemin = "-1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemin))<1):
    diemin = "-1";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"u"+diemin+":"+diemax;
  if(child.tag=="coin"):
   if(diestr!=""):
    diestr = diestr+",";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"c";
 return RandomRollMultiDiceNotationMinMaxByString(diestr, RandType, RandSeed);

def RandomRollMultiDieMinMaxByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceMinMaxByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceNotationByString(DiceStr="1d6", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("([0-9]*)c([\+\-\*\/]?[0-9\+\-\*\/]*)", "\\1d2\\2", DiceStr);
 DiceStr = DiceStr.replace("x", "*");
 DiceStr = DiceStr.replace("×", "*");
 DiceStr = DiceStr.replace("÷", "/");
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetPreDiceRoll = re.findall("([0-9]*)d([\-]?[0-9]+)([l|h]?[0-9]*)([\+\-\*\/]?[0-9\+\-\*\/]*)([l|h]?[0-9]*)", DiceStrList[CountNumOfDice])[0];
  if(GetPreDiceRoll[0]==""):
   GetNumDice = 1;
  else:
   GetNumDice = int(GetPreDiceRoll[0]);
  GetNewDiceRoll = int(GetPreDiceRoll[1]);
  DiceRollSum = str(GetPreDiceRoll[3]);
  GetDiceAVGList = "";
  if(not GetPreDiceRoll[2]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[2]))>0):
    GetDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[2])[0];
   else:
    GetPreDiceRoll[2] = "";
  GetPreDiceRollList = [];
  GetSubDiceRollList = [];
  if(GetNumDice>0):
   GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDiceAlt(GetNumDice, GetNewDiceRoll, RandType, RandSeed);
  if(GetPreDiceRoll[2]==""):
   GetSubDiceRollList = GetPreDiceRollList;
  else:
   if(int(GetDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetDiceAVGList[0]=="l"):
    GetSubDiceRollList = GetMinValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   if(GetDiceAVGList[0]=="h"):
    GetSubDiceRollList = GetMaxValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
  SubNumOfDice = len(GetSubDiceRollList);
  GetDiceRollList = [];
  SubCountNumOfDice = 0;
  while(SubCountNumOfDice<SubNumOfDice):
   NeoPreDiceRoll = str(GetSubDiceRollList[SubCountNumOfDice]);
   GetDiceRollList.append(int(eval(NeoPreDiceRoll+DiceRollSum)));
   SubCountNumOfDice = SubCountNumOfDice + 1;
  GetLastDiceRollList = [];
  GetPostDiceAVGList = "";
  if(not GetPreDiceRoll[4]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[4]))>0):
    GetPostDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[4])[0];
   else:
    GetPreDiceRoll[4] = "";
  if(GetPreDiceRoll[4]==""):
   GetLastDiceRollList = GetDiceRollList;
  else:
   if(int(GetPostDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetPostDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetPostDiceAVGList[0]=="l"):
    GetLastDiceRollList = GetMinValues(GetDiceRollList, int(GetPostDiceAVGList[1]));
   if(GetPostDiceAVGList[0]=="h"):
    GetLastDiceRollList = GetMaxValues(GetDiceRollList, int(GetPostDiceAVGList[1]));
  DiceRolls = DiceRolls + GetLastDiceRollList;
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDieNotationByString(DieStr="1d6", RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceNotationByString(DieStr, RandType, RandSeed);

def RandomRollMultiDiceNotationByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   dieexp = "";
   if('exp' in child.attrib):
     dieexp = str(child.attrib['exp']);
   else:
    dieexp = "";
   if(len(re.findall("^([\+\-\*\/]?[0-9\+\-\*\/]*)$", dieexp))<1):
    dieexp = "";
   diestr = diestr+dienum+"d"+diemax+dieexp;
 return RandomRollMultiDiceNotationMinMaxByString(diestr, RandType, RandSeed);

def RandomRollMultiDieNotationByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceNotationByXML(DieStrFile, RandType, RandSeed);

def RandomRollMultiDiceNotationMinMaxByString(DiceStr="1d1:6", RandType=1, RandSeed=random.seed()):
 DiceStr = DiceStr.strip();
 DiceStr = DiceStr.lower();
 DiceStr = re.sub("([0-9]*)c([\+\-\*\/]?[0-9\+\-\*\/]*)", "\\1d1:2\\2", DiceStr);
 DiceStr = re.sub("([0-9]*)u([0-9]+)([l|h]?[0-9]*)([\+\-\*\/]?[0-9\+\-\*\/]*)([l|h]?[0-9]*)", "\\1d-\\2:\\2\\3\\4\\5", DiceStr);
 DiceStr = DiceStr.replace("x", "*");
 DiceStr = DiceStr.replace("×", "*");
 DiceStr = DiceStr.replace("÷", "/");
 DiceStrList = DiceStr.split(",");
 NumOfDice = len(DiceStrList);
 CountNumOfDice = 0;
 DiceRolls = [];
 while(CountNumOfDice<NumOfDice):
  GetPreDiceRoll = re.findall("([0-9]*)d([\-]?[0-9]+)([\:]?[\-]?[0-9]*)([l|h]?[0-9]*)([\+\-\*\/]?[0-9\+\-\*\/]*)([l|h]?[0-9]*)", DiceStrList[CountNumOfDice])[0];
  if(GetPreDiceRoll[0]==""):
   GetNumDice = 1;
  else:
   GetNumDice = int(GetPreDiceRoll[0]);
  GetMinDiceRoll = int(GetPreDiceRoll[1]);
  GetPreMaxDiceRoll = GetPreDiceRoll[2].replace(":", "");
  if(GetPreMaxDiceRoll==""):
   GetMaxDiceRoll = "";
  else:
   GetMaxDiceRoll = int(GetPreMaxDiceRoll);
  DiceRollSum = str(GetPreDiceRoll[4]);
  GetDiceAVGList = "";
  if(not GetPreDiceRoll[3]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[3]))>0):
    GetDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[3])[0];
   else:
    GetPreDiceRoll[3] = "";
  GetPreDiceRollList = [];
  GetSubDiceRollList = [];
  if(GetNumDice>0):
   if(GetMaxDiceRoll==""):
    GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDiceAlt(GetNumDice, GetMinDiceRoll, RandType, RandSeed);
   else:
    GetPreDiceRollList = GetPreDiceRollList + RandomRollMultiSameDice(GetNumDice, GetMinDiceRoll, GetMaxDiceRoll, RandType, RandSeed);
  if(GetPreDiceRoll[3]==""):
   GetSubDiceRollList = GetPreDiceRollList;
  else:
   if(int(GetDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetDiceAVGList[0]=="l"):
    GetSubDiceRollList = GetMinValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
   if(GetDiceAVGList[0]=="h"):
    GetSubDiceRollList = GetMaxValues(GetPreDiceRollList, int(GetDiceAVGList[1]));
  SubNumOfDice = len(GetSubDiceRollList);
  GetDiceRollList = [];
  SubCountNumOfDice = 0;
  while(SubCountNumOfDice<SubNumOfDice):
   NeoPreDiceRoll = str(GetSubDiceRollList[SubCountNumOfDice]);
   GetDiceRollList.append(int(eval(NeoPreDiceRoll+DiceRollSum)));
   SubCountNumOfDice = SubCountNumOfDice + 1;
  GetLastDiceRollList = [];
  GetPostDiceAVGList = "";
  if(not GetPreDiceRoll[5]==""):
   if(len(re.findall("^([l|h]{1})([0-9]+)$",  GetPreDiceRoll[5]))>0):
    GetPostDiceAVGList = re.findall("^([l|h]{1})([0-9]+)$", GetPreDiceRoll[5])[0];
   else:
    GetPreDiceRoll[5] = "";
  if(GetPreDiceRoll[5]==""):
   GetLastDiceRollList = GetDiceRollList;
  else:
   if(int(GetPostDiceAVGList[1])>int(GetPreDiceRoll[0])):
    GetPostDiceAVGList[1] = GetPreDiceRoll[0];
   if(GetPostDiceAVGList[0]=="l"):
    GetLastDiceRollList = GetMinValues(GetDiceRollList, int(GetPostDiceAVGList[1]));
   if(GetPostDiceAVGList[0]=="h"):
    GetLastDiceRollList = GetMaxValues(GetDiceRollList, int(GetPostDiceAVGList[1]));
  DiceRolls = DiceRolls + GetLastDiceRollList;
  CountNumOfDice = CountNumOfDice + 1;
 return DiceRolls;

def RandomRollMultiDieNotationMinMaxByString(DieStr="1d1:6", RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceNotationMinMaxByString(DieStr, RandType, RandSeed);

def RandomRollMultiDiceNotationMinMaxByXML(DiceStrFile, RandType=1, RandSeed=random.seed()):
 diestr = "";
 tree = cElementTree.ElementTree(file=DiceStrFile);
 root = tree.getroot();
 for child in root:
  if(child.tag=="dice"):
   if(diestr!=""):
    diestr = diestr+",";
   if('min' in child.attrib):
    diemin = str(child.attrib['min']);
   else:
    diemin = "1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemin))<1):
    diemin = "1";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
   else:
    diemax = "6";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "6";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   dieexp = "";
   if('exp' in child.attrib):
     dieexp = str(child.attrib['exp']);
   else:
    dieexp = "";
   if(len(re.findall("^([\+\-\*\/]?[0-9\+\-\*\/]*)$", dieexp))<1):
    dieexp = "";
  if(child.tag=="fudge"):
   if(diestr!=""):
    diestr = diestr+",";
   diemin = "";
   diemax = "";
   if('max' in child.attrib):
    diemax = str(child.attrib['max']);
    diemin = "-"+str(child.attrib['max']);
   else:
    diemax = "1";
    diemin = "-1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemax))<1):
    diemax = "1";
   if(len(re.findall("^([\-]?[0-9]+)$", diemin))<1):
    diemin = "-1";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   dieexp = "";
   if('exp' in child.attrib):
     dieexp = str(child.attrib['exp']);
   else:
    dieexp = "";
   if(len(re.findall("^([\+\-\*\/]?[0-9\+\-\*\/]*)$", dieexp))<1):
    dieexp = "";
   diestr = diestr+dienum+"u"+diemin+":"+diemax+dieexp;
  if(child.tag=="coin"):
   if(diestr!=""):
    diestr = diestr+",";
   dienum = "";
   if('num' in child.attrib):
    dienum = str(child.attrib['num']);
   else:
    dienum = "1";
   if(len(re.findall("^([0-9]+)$", dienum))<1):
    dienum = "1";
   diestr = diestr+dienum+"c";
   dieexp = "";
   if('exp' in child.attrib):
     dieexp = str(child.attrib['exp']);
   else:
    dieexp = "";
   if(len(re.findall("^([\+\-\*\/]?[0-9\+\-\*\/]*)$", dieexp))<1):
    dieexp = "";
   diestr = diestr+dienum+"d"+diemin+":"+diemax+dieexp;
 return RandomRollMultiDiceNotationMinMaxByString(diestr, RandType, RandSeed);

def RandomRollMultiDieNotationMinMaxByXML(DieStrFile, RandType=1, RandSeed=random.seed()):
 return RandomRollMultiDiceNotationMinMaxByXML(DieStrFile, RandType, RandSeed);

def RandomCoinFlip(ReturnValType="int", RandType=1, RandSeed=random.seed()):
 ReturnValType = ReturnValType.lower();
 CoinFlip = RandomDiceRollAlt(2, RandType, RandSeed);
 if(ReturnValType=="int" or ReturnValType=="integer"):
  CoinFlipValue = CoinFlip[0];
 if(ReturnValType=="bool" or ReturnValType=="boolean"):
  if(CoinFlipValue==1):
   CoinFlipValue = True;
  if(CoinFlipValue==2):
   CoinFlipValue = False;
 if(ReturnValType=="str" or ReturnValType=="string"):
  if(CoinFlipValue==1):
   CoinFlipValue = "Heads";
  if(CoinFlipValue==2):
   CoinFlipValue = "Tails";
 return [CoinFlipValue];

def RandomMultiCoinFlip(NumOfCoins=1, ReturnValType="int", RandType=1, RandSeed=random.seed()):
 CountNumOfCoins = 0;
 CoinFlipValue = [];
 while(CountNumOfCoins<NumOfCoins):
  CoinFlipValue = CoinFlipValue + RandomCoinFlip(ReturnValType, RandType, RandSeed);
  CountNumOfCoins = CountNumOfCoins + 1;
 return CoinFlipValue;
