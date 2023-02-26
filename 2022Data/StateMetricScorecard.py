from numpy.core.numeric import NaN
import pandas as pd


"""
# National averages for 2021

NA_PHSWCS = 0.5130 # National average - % HS with CS
NA_PSHSWCS = 0.7770 # National average - % Students in HS with CS
NA_HNHHSSR = 0.302 # National average - Have Not/Have HS Size Ratio
NA_PRHSWCSR = 0.765 # National average - Poor/Rich HS with CS Ratio
NA_RUHSWCSR = 0.884 # National average - Rural/Urban HS with CS Ratio

NA_PSEICS = 0.0471   # National average - % Students Enrolled in CS
NA_FUR = .0593 # National average - Students Enrolled in CS / Students in HS with CS (FCS Uptake Ratio)
NA_PSTAPCSE = 0.0108 # National average - Students taking AP CS Exam
NA_APCSFCSUR = 0.2241 #  National average - Students Taking AP CS Exam / Students Enrolled in CS
NA_APCSSHSUR = 0.0139 #  National average - Students Taking AP CS Exam / Students in HS with CS
NA_PRATIO = 0.634 #  National average - P Ratio (P / (A + P))
NA_APCSPR = 0.705 #  National average - AP CS Pass Rate (All)
NA_APCSPPR = 0.713 #  National average - AP CSP Pass Rate
NA_APCSAPR = 0.692 #  National average - AP CSA Pass RAte

NA_PSHSWCS_RSWM = 1.00 # National average - % Students in HS with CS - Relative Strength - Women/Men
NA_FUR_RSWM =0.4729 # National average - FCS Uptake Ratio - Relative Strength - Women/Men
NA_APCSFCSUR_RSWM = 0.9843 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Women/Men
NA_APCSSHSUR_RSWM = 0.4610 #  National average - Students Taking AP CS Exam / Students in HS with CS - Women/Men
NA_APCSPR_RSWM = 1.0308 #  National average - AP CS Pass Rate (All) - Relative Strength - Women/Men

NA_PSHSWCS_RSBW = 0.9267 # National average - % Students in HS with CS - Relative Strength - Black/White
NA_FUR_RSBW =1.0622 # National average - FCS Uptake Ratio - Relative Strength - Black/White
NA_APCSFCSUR_RSBW = 0.4465 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Black/White
NA_APCSSHSUR_RSBW = 0.4679 #  National average - Students Taking AP CS Exam / Students in HS with CS - Black/White
NA_APCSPR_RSBW = 0.6413 #  National average - AP CS Pass Rate (All) - Relative Strength - Black/White

NA_PSHSWCS_RSHLW = 0.9599 # National average - % Students in HS with CS - Relative Strength - Hispanic-Latinx/White
NA_FUR_RSHLW =0.7918 # National average - FCS Uptake Ratio - Relative Strength - Hispanic-Latinx/White
NA_APCSFCSUR_RSHLW = 0.8819 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Hispanic-Latinx/White
NA_APCSSHSUR_RSHLW = 0.7040 #  National average - Students Taking AP CS Exam / Students in HS with CS - Hispanic-Latinx/White
NA_APCSPR_RSHLW = 0.7726 #  National average - AP CS Pass Rate (All) - Relative Strength - Hispanic-Latinx/White
"""

# National averages for 2022


NA_PHSWCS = 0.5130 # National average - % HS with CS *
NA_PSHSWCS = 0.7481 # National average - % Students in HS with CS *
NA_HNHHSSR = 0.3808 # National average - Have Not/Have HS Size Ratio 
NA_PRHSWCSR = 0.7670 # National average - Poor/Rich HS with CS Ratio 
NA_RUHSWCSR = 1.2162 # National average - Rural/Urban HS with CS Ratio 

NA_PSEICS = 0.0559   # National average - % Students Enrolled in CS *
NA_FUR = .0729 # National average - Students Enrolled in CS / Students in HS with CS (FCS Uptake Ratio) *
NA_PSTAPCSE = 0.0105 # National average - Students taking AP CS Exam *
NA_APCSFCSUR = 0.1834 #  National average - Students Taking AP CS Exam / Students Enrolled in CS *
NA_APCSSHSUR = 0.0140 #  National average - Students Taking AP CS Exam / Students in HS with CS *
NA_PRATIO = 0.6265 #  National average - P Ratio (P / (A + P)) *
NA_APCSPR = 0.6538 #  National average - AP CS Pass Rate (All) *
NA_APCSPPR = 0.6615 #  National average - AP CSP Pass Rate *
NA_APCSAPR = 0.6406 #  National average - AP CSA Pass RAte *

NA_PSHSWCS_RSWM = 1.00 # National average - % Students in HS with CS - Relative Strength - Women/Men - * still 1.0
NA_FUR_RSWM =0.4798 # National average - FCS Uptake Ratio - Relative Strength - Women/Men *
NA_APCSFCSUR_RSWM = 0.9731 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Women/Men *
NA_APCSSHSUR_RSWM = 0.4603 #  National average - Students Taking AP CS Exam / Students in HS with CS - Women/Men *
NA_APCSPR_RSWM = 0.9644 #  National average - AP CS Pass Rate (All) - Relative Strength - Women/Men

NA_PSHSWCS_RSBW = 0.9201 # National average - % Students in HS with CS - Relative Strength - Black/White *
NA_FUR_RSBW =1.0551 # National average - FCS Uptake Ratio - Relative Strength - Black/White *
NA_APCSFCSUR_RSBW = 0.5157 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Black/White *
NA_APCSSHSUR_RSBW = 0.5191 #  National average - Students Taking AP CS Exam / Students in HS with CS - Black/White *
NA_APCSPR_RSBW = 0.4662 #  National average - AP CS Pass Rate (All) - Relative Strength - Black/White

NA_PSHSWCS_RSHLW = 0.9456 # National average - % Students in HS with CS - Relative Strength - Hispanic-Latinx/White *
NA_FUR_RSHLW =0.8099 # National average - FCS Uptake Ratio - Relative Strength - Hispanic-Latinx/White *
NA_APCSFCSUR_RSHLW = 0.9162 #  National average - Students Taking AP CS Exam / Students Enrolled in CS - Relative Strength - Hispanic-Latinx/White *
NA_APCSSHSUR_RSHLW = 0.7149 #  National average - Students Taking AP CS Exam / Students in HS with CS - Hispanic-Latinx/White *
NA_APCSPR_RSHLW = 0.6328 #  National average - AP CS Pass Rate (All) - Relative Strength - Hispanic-Latinx/White

def writeHTMLhead(state_file, state_name, css):
    state_file.write("<!DOCTYPE html>\n") 
    state_file.write("<html>\n")
    state_file.write("<head>\n")
    state_file.write("    <title>" + state_name + "</title>\n")
    #state_file.write('    <link rel="stylesheet" href="cstadata.css">\n')
    state_file.write('<style>\n' + css + "\n</style>\n")
    state_file.write("</head>\n")
    state_file.write("<body>\n")
    state_file.write("<h1>CS Education Metrics Scorecard for " + state_name + " (2022)</h1>\n")
    state_file.write("<p>For more information on this scorecard, visit <br><a href='https://cranidores.org/cs-education-analytics/state-specific-computer-science-education-scorecards-2022/'>https://cranidores.org/cs-education-analytics/state-specific-computer-science-education-scorecards-2022/</a></p>\n")


def writeHTMLfoot(state_file):
    state_file.write("</body>\n")
    state_file.write("</html>\n")

def writeTablehead(state_file, state_name):
    state_file.write("<thead>\n")
    state_file.write("<tr>\n")
    state_file.write("    <th width='40%'>Statistic</th>\n")
    state_file.write("    <th width='20%'>Nationwide</th>\n")
    state_file.write("    <th width='20%'>" + state_name + "</th>\n")
    state_file.write("    <th width='20%'>Z-Score</th>\n")
    state_file.write("</tr>\n")
    state_file.write("</thead>\n")

def getrowcolor(zscore):

    if ((type(zscore) != float) and (zscore.isnull().any())): 
        return "nostat"
    else:
        zscore =float(zscore)
      
    if (zscore < -2):
        return "low3val"
    elif (zscore < -1.25):
        return "low2val"
    elif (zscore < -0.5):
        return "low1val"
    elif (zscore < 0.5):
        return "avgval"
    elif (zscore < 1.25):
        return "high1val"
    elif (zscore < 2):
        return "high2val"
    else:
        return "high3val"

def stringValFmtPct(inputval):
    if (type(inputval) != float) and (inputval.isnull().any()):
        return " - "
    return '{:.1f}%'.format(100 * float(inputval))

def stringValFmt(inputval):
    if (type(inputval) != float) and (inputval.isnull().any()):
        return " - "
    return '{:.2f}'.format(float(inputval))

def writeStateline(state_file, stat_name, nat_stat, state_stat, z_score):
    state_file.write("<tr class='" + getrowcolor(z_score) + "'>\n")
    state_file.write("    <td>" + stat_name + "</td>\n")
    state_file.write("    <td class='ncenter'>" + stringValFmtPct(nat_stat) + "</td>\n")
    state_file.write("    <td class='ncenter'>" + stringValFmtPct(state_stat) + "</td>\n")
    state_file.write("    <td class='ncenter'>" + stringValFmt(z_score) + "</td>\n")
    state_file.write("</tr>\n")


def writeSchoolstats(state_file, state_name, school_row, student_row):
    state_file.write("<h2>School-Based Statistics</h2>\n")
    state_file.write("<table>\n")
    writeTablehead(state_file, state_name)
    state_file.write("<tbody>\n")
    writeStateline(state_file, "% HS with CS", NA_PHSWCS, student_row['PctHSwFCS'],  student_row['ZScore_PctHSwFCS'])
    writeStateline(state_file, "% Students in HS with CS", NA_PSHSWCS, student_row['PctStudentsHSwCS'],  student_row['ZScore_PctStudentsHSwCS'])
    writeStateline(state_file, "Have Not/Have HS Size Ratio", NA_HNHHSSR, school_row['HaveNotCSHaveCS_Size_Ratio'], school_row['HaveNotCSHaveCS_Size_Ratio_Zscore'])
    writeStateline(state_file, "Poor/Rich HS with CS Ratio", NA_PRHSWCSR, school_row['RS_FRLInc_FCS_School'], school_row['RS_FRLInc_FCS_School_Zscore'])
    writeStateline(state_file, "Rural/Urban HS with CS Ratio", NA_RUHSWCSR, school_row['RS_RuralUrban_FCS_School'], school_row['RS_RuralUrban_FCS_School_Zscore'])
    state_file.write("</tbody>\n")
    state_file.write("</table>\n")
    state_file.write("<p></p><p></p>\n")



def writeStudentstats(state_file, state_name, state_row_ap, student_row):
    state_file.write("<h2>Student-Based Statistics</h2>\n")
    state_file.write("<table>\n")
    writeTablehead(state_file, state_name)
    state_file.write("<tbody>\n")
    writeStateline(state_file, "% Students in HS with CS", NA_PSHSWCS, student_row['PctStudentsHSwCS'], student_row['ZScore_PctStudentsHSwCS'])
    writeStateline(state_file, "% Students Enrolled in CS", NA_PSEICS,  student_row['Pct_InFCS'], student_row['ZScore_Pct_InFCS'])
    writeStateline(state_file, "Students Enrolled in CS /<br/>Students in HS with CS", NA_FUR, student_row['CP_StFCS_StHSCS_All'], student_row['ZScore_CP_StFCS_StHSCS_All'])
    writeStateline(state_file, "% Students taking AP CS Exam", NA_PSTAPCSE,  student_row['Pct_InAP'], student_row['ZScore_Pct_InAP'])
    writeStateline(state_file, "Students Taking AP CS Exam /<br/>Students Enrolled in CS", NA_APCSFCSUR,  student_row['CP_StAP_StFCS_All'], student_row['ZScore_CP_StAP_StFCS_All'])
    writeStateline(state_file, "Students Taking AP CS Exam /<br/>Students in HS with CS", NA_APCSSHSUR,  student_row['CP_StAP_StHSCS_All'], student_row['ZScore_CP_StAP_StHSCS_All'])
    writeStateline(state_file, "P Ratio (P / (A + P))", NA_PRATIO, state_row_ap['PRatio'], state_row_ap['PRatio_ZS'])
    writeStateline(state_file, "AP CS Pass Rate", NA_APCSPR, state_row_ap['PnA_Total_PassRate'], state_row_ap['PnA_Total_PassRate_ZS'])
    writeStateline(state_file, "AP CSP Pass Rate", NA_APCSPPR, state_row_ap['P_Total_PassRate'], state_row_ap['P_Total_PassRate_ZS'])
    writeStateline(state_file, "AP CSA Pass Rate", NA_APCSAPR, state_row_ap['A_Total_PassRate'], state_row_ap['A_Total_PassRate_ZS'])
    state_file.write("</tbody>\n")
    state_file.write("</table>\n")
    state_file.write("<p></p><p></p>\n")

def createRSNAframe(pPSHSWCS, pFUR, pAPCSFCSUR, pAPCSSHSUR, pAPCSPR):
    return pd.DataFrame([
            {'PSHSWCS': pPSHSWCS,
             'FUR': pFUR,
             'APCSFCSUR': pAPCSFCSUR,
             'APCSSHSUR': pAPCSSHSUR,
             'APCSPR': pAPCSPR
            }
        ])

def createRSStateframe(df_state, df_state_ap, rsgroup):
        dict_state = df_state.iloc[0].to_dict()
        #dict_ap = df_state_ap.iloc[0].to_dict()
        return pd.DataFrame([
            {
             'PSHSWCS': dict_state["RS_" + rsgroup + "_CP_StHSCS_HSCS"],
             'FUR': dict_state["RS_"+ rsgroup + "_CP_StFCS_StHSCS"],
             'APCSFCSUR': dict_state["RS_" + rsgroup + "_CP_StAP_StFCS"],
             'APCSSHSUR': dict_state["RS_" + rsgroup + "_CP_StAP_StHSCS"],
             'APCSPR': df_state_ap["RS_" + rsgroup + "_PnA_PassRate"],
             'ZS_PSHSWCS': dict_state["ZScore_RS_" + rsgroup + "_CP_StHSCS_HSCS"],
             'ZS_FUR': dict_state["ZScore_RS_"+ rsgroup + "_CP_StFCS_StHSCS"],
             'ZS_APCSFCSUR': dict_state["ZScore_RS_" + rsgroup + "_CP_StAP_StFCS"],
             'ZS_APCSSHSUR': dict_state["ZScore_RS_" + rsgroup + "_CP_StAP_StHSCS"],
             'ZS_APCSPR': df_state_ap["RS_" + rsgroup + "_PnA_PassRate_ZS"]
            }
        ])


def writeRelStrengthGroup(state_file, group_name, state_name, df_natavg, df_staterow):
    state_file.write("<h2>" + group_name + " Relative Strength Statistics</h2>\n")
    state_file.write("<table>\n")
    writeTablehead(state_file, state_name)
    state_file.write("<tbody>\n")
    writeStateline(state_file, "% Students in HS with CS", df_natavg['PSHSWCS'],  df_staterow['PSHSWCS'],  df_staterow['ZS_PSHSWCS'])
    writeStateline(state_file, "Students Enrolled in CS /<br/>Students in HS with CS", df_natavg['FUR'], df_staterow['FUR'], df_staterow['ZS_FUR'])
    writeStateline(state_file, "Students taking AP CS Exam /<br/>Students Enrolled in CS", df_natavg['APCSFCSUR'], df_staterow['APCSFCSUR'], df_staterow['ZS_APCSFCSUR'])
    writeStateline(state_file, "Students Taking AP CS Exam /<br/>Students in HS with CS", df_natavg['APCSSHSUR'], df_staterow['APCSSHSUR'], df_staterow['ZS_APCSSHSUR'])
    writeStateline(state_file, "AP CS Pass Rate", df_natavg['APCSPR'], df_staterow['APCSPR'], df_staterow['ZS_APCSPR'])
    state_file.write("</tbody>\n")
    state_file.write("</table>\n")
    state_file.write("<p></p><p></p>\n")

"""
Start of main code here
"""

# Read CSS
css_file = open("cstadata.css")
css_contents = css_file.read()


# Read data files      
dfSchool = pd.read_csv('SchoolBasedDatafor2022.csv')
dfAPState = pd.read_csv('APCSbyStateFor2022.csv')
dfStudent = pd.read_csv('StudentKeyMetricsfor2022.csv')

# Convert objects to strings in dataframe
dfSchool['StateAbbv'] = dfSchool['StateAbbv'].astype(str)
dfAPState['StateAbbv'] = dfAPState['StateAbbv'].astype(str)
dfAPState['StateName'] = dfAPState['StateName'].astype(str)
dfStudent['StateAbbv'] = dfStudent['StateAbbv'].astype(str)
dfStudent['StateName'] = dfStudent['StateName'].astype(str)

# Rename columns so they will be consistent for use in various functions
dfStudent.rename(columns = {'RS_FemaleMaleEst_CP_StFCS_StHSCS':'RS_FemaleMale_CP_StFCS_StHSCS'}, inplace = True)
dfStudent.rename(columns = {'RS_FemaleMaleEst_CP_StAP_StHSCS':'RS_FemaleMale_CP_StAP_StHSCS'}, inplace = True)
dfStudent.rename(columns = {'ZScore_RS_FemaleMaleEst_CP_StFCS_StHSCS':'ZScore_RS_FemaleMale_CP_StFCS_StHSCS'}, inplace = True)
dfStudent.rename(columns = {'ZScore_RS_FemaleMaleEst_CP_StAP_StHSCS':'ZScore_RS_FemaleMale_CP_StAP_StHSCS'}, inplace = True)
dfStudent['RS_FemaleMale_CP_StHSCS_HSCS'] = NaN
dfStudent['ZScore_RS_FemaleMale_CP_StHSCS_HSCS'] = NaN
dfAPState.rename(columns = {'RS_HispanicWhite_PnA_PassRate':'RS_HLLLWhite_PnA_PassRate'}, inplace = True)
dfAPState.rename(columns = {'RS_HispanicWhite_PnA_PassRate_ZS':'RS_HLLLWhite_PnA_PassRate_ZS'}, inplace = True)

# copy columns so can fit into work later

for ndx, staterow_ap in dfAPState.iterrows():
    stateName, stateAbbv  = staterow_ap[['StateName', 'StateAbbv']]
    stateFilename = stateName.replace(" ","") + ".html"
    print (stateAbbv)

    staterow_school = dfSchool.loc[dfSchool['StateAbbv']==stateAbbv].copy()
    staterow_student = dfStudent.loc[dfStudent['StateAbbv']==stateAbbv].copy()
          
    state_file = open(stateFilename, "w")
    writeHTMLhead(state_file,stateName, css_contents)
    writeSchoolstats(state_file, stateName, staterow_school, staterow_student) 
    writeStudentstats(state_file, stateName, staterow_ap, staterow_student)

    dfRSWMnatavg = createRSNAframe(NA_PSHSWCS_RSWM, NA_FUR_RSWM, NA_APCSFCSUR_RSWM, NA_APCSSHSUR_RSWM, NA_APCSPR_RSWM)
    dfRSWMstate = createRSStateframe(staterow_student, staterow_ap, "FemaleMale")
    writeRelStrengthGroup(state_file, "Women/Men", stateName, dfRSWMnatavg, dfRSWMstate)

    dfRSBWnatavg = createRSNAframe(NA_PSHSWCS_RSBW, NA_FUR_RSBW, NA_APCSFCSUR_RSBW, NA_APCSSHSUR_RSBW, NA_APCSPR_RSBW)
    dfRSBWstate = createRSStateframe(staterow_student, staterow_ap, "BlackWhite")
    writeRelStrengthGroup(state_file, "Black/White", stateName, dfRSBWnatavg, dfRSBWstate)

    dfRSHLWnatavg = createRSNAframe(NA_PSHSWCS_RSHLW, NA_FUR_RSHLW, NA_APCSFCSUR_RSHLW, NA_APCSSHSUR_RSHLW, NA_APCSPR_RSHLW)
    dfRSHLWstate = createRSStateframe(staterow_student, staterow_ap, "HLLLWhite")
    writeRelStrengthGroup(state_file, "Hispanic-Latinx/White", stateName, dfRSHLWnatavg, dfRSHLWstate)
 
    writeHTMLfoot(state_file)
    state_file.close()

