import pandas as pd
sheet_id="1fbFp2IIFK4APGMAnl31kouZhYNsH0Ll7kbgxMH_J6B8"
# this is the key for the doc, hopefully does not change. Will edit as needed
url = f"https://docs.google.com/spreadsheets/d/1fbFp2IIFK4APGMAnl31kouZhYNsH0Ll7kbgxMH_J6B8/export?format=csv"
# copy the link up until edit, remove beyond that and add the export info
uma=pd.read_csv(url)
uma['Uma']=uma['Uma'].str.upper()
uma.shape
umasmol=uma.drop(columns = ['Uma', 'Height diff','Bust diff','Waist diff','Hips diff','Shortstack Score','Tallboard Score','TBHS',
                            'Hourglass Quotient','Oatmeal%','Donk Rating','Todo Index'])
umasmol.head()
explodegoal=umasmol.mean()
explodegoal.head()
explodemeans = [82.570423, 55.535211, 81.873239, 158.521127] 
# means from above
cols_to_check = ['Bust', 'Waist', 'Hips', 'Height']
# what columns we checking
distances = (uma[cols_to_check] - explodemeans).pow(2).sum(axis=1)
# distance from each
closest_row_index = distances.idxmin()
# index that binch
closest_row = uma.loc[closest_row_index]
# profit
print(f"The most average uma is {closest_row_index}:")
print(closest_row)

uma.nlargest(5, 'Bust')
# top 5 bustiest umas

uma.nsmallest(5, 'Bust')
# top 5 flattest umas

uma.nlargest(5, 'Waist')

uma.nlargest(5, 'Hips')

uma.nlargest(5, 'Height')

uma.nlargest(5, 'Height diff')

uma.nlargest(5, 'Bust diff')

uma.nlargest(5, 'Waist diff')

uma.nlargest(5, 'Hips diff')

uma.nlargest(5, 'Shortstack Score')

uma.nlargest(5, 'Tallboard Score')

uma.nlargest(5, 'TBHS')
# most top heavy

uma.nsmallest(5, 'TBHS')
# most bottom heavy

uma.nlargest(5, 'Hourglass Quotient')

uma['Oatmeal%'] = uma['Oatmeal%'].str.replace('%', '').astype(float)
uma.nlargest(5, 'Oatmeal%')

uma.nlargest(5, 'Donk Rating')

uma.nlargest(5, 'Todo Index')

# so this will be a lot more.... subjective? This will give general ratios that the secondary scores follow. 
bustratio=uma['Bust']/uma['Height']
bustratioM=bustratio.mean()
bustratioSTD=bustratio.std()
print(f"An uma's bust, on average, should be around: {bustratioM:.1%} of their height.")

waistratio=uma['Waist']/uma['Height']
waistratioM=waistratio.mean()
waistratioSTD=waistratio.std()
print(f"An uma's waist, on average, should be around: {waistratioM:.1%} of their height.")

hipsratio=uma['Hips']/uma['Height']
hipsratioM=hipsratio.mean()
hipsratioSTD=hipsratio.std()
print(f"An uma's hips, on average, should be around: {hipsratioM:.1%} of their height.")
