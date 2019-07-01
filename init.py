from flask import Flask, render_template,url_for,request
from wtforms import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length, Email

from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'locked'
app.config['MYSQL_DB'] = 'ficcidb'

mysql = MySQL(app)

@app.route("/",methods=['GET','POST'])
def Ficci():
	if request.method=="POST":
		details=request.form
		NameAndDesignation=details['namee']				
		CompanyName=details['desig']
		Email=details['email']
		Mobile=details['mobile']
		GDPGrowthRateAtMarketPricesQ4=details['sec1a']
		GDPGrowthRateAtMarketPricesQ1=details['sec1b']
		GDPGrowthRateAtMarketPrices2019and2020=details['sec1c']
		GDPGrowthRateAtMarketPrices2020and2020=details['sec1d']
		GVAAtBasicPricesAtConstantPricesQ4=details['sec2a']
		GVAAtBasicPricesAtConstantPricesQ1=details['sec2b']
		GVAAtBasicPricesAtConstantPrices2019and2020=details['sec2c']
		GVAAtBasicPricesAtConstantPrices2020and2021=details['sec2d']
		GrossDomesticSavingQ4=details['sec3a']
		GrossDomesticSavingQ1=details['sec3b']
		GrossDomesticSaving2019And2020=details['sec3c']
		GrossDomesticSaving2020and2021=details['sec3d']
		GrossFixedCapitalFormationQ4=details['sec4a']
		GrossFixedCapitalFormationQ1=details['sec4b']
		GrossFixedCapitalFormation2019and2020=details['sec4c']
		GrossFixedCapitalFormation2020and2021=details['sec4d']
		FiscalDeficitQ4=details['sec5a']
		FiscalDeficitQ1=details['sec5b']
		FiscalDeficit2019and2020=details['sec5c']
		FiscalDeficit2020and2021=details['sec5d']
		GrowthInIIPQ4=details['sec6a']
		GrowthInIIPQ1=details['sec6b']
		GrowthInIIP2019and2020=details['sec6c']
		GrowthInIIP2020and21=details['sec6d']
		WPIAllCommoditiesInflationRateQ4=details['sec7a']
		WPIAllCommoditiesInflationRateQ1=details['sec7b']
		WPIAllCommoditiesInflationRate2019and2020=details['sec7c']
		WPIAllCommoditiesInflationRate2020and2021=details['sec7d']
		CPICombinedNewInflationRateQ4=details['sec8a']
		CPICombinedNewInflationRateQ1=details['sec8b']
		CPICombinedNewInflationRate2019and2020=details['sec8c']
		CPICombinedNewInflationrate2020and2021=details['sec8d']
		PrimeLendingRateQ4=details['sec9a']
		PrimeLendingRateQ1=details['sec9b']
		PrimeLendingRate2019and2020=details['sec9c']
		PrimeLendingRate2020and2021=details['sec9d']
		MoneySupplyGrowthQ4=details['sec10a']
		MoneySupplyGrowthQ1=details['sec10b']
		MoneySupplyGrowth2019and2020=details['sec10c']
		MoneySupplyGrowth2020and2021=details['sec10d']
		BankCreditGrowthQ4=details['sec11a']
		BankCreditGrowthQ1=details['sec11b']
		BankCreditGrowth2019and2020=details['sec11c']
		BankCreditGrowth2020and2021=details['sec11d']
		RepoRateQ4=details['sec12a']
		RepoRateQ1=details['sec12b']
		RepoRate2019and2020=details['sec12c']
		RepoRate2020and2021=details['sec12d']
		MerchandiseExportQ4=details['sec13e']
		MerchandiseExportQ1=details['sec13f']
		MerchandiseExport2019and2020=details['sec13g']
		MerchandiseExport2020and2021=details['sec13h']
		MerchandiseImportQ4=details['sec14e']
		MerchandiseImportQ1=details['sec14f']
		MerchandiseImport2019and2020=details['sec14g']
		MerchandiseImport2020and2021=details['sec14h']
		TradeBalanceQ4=details['sec15a']
		TradeBalanceQ1=details['sec15b']
		TradeBalance2019and2020=details['sec15c']
		TradeBalance2020and2021=details['sec15d']
		CurrentAccountBalanceQ4=details['sec16e']
		CurrentAccountBalanceQ1=details['sec16f']
		CurrentAccountBalance2019and2020=details['sec16g']
		CurrentAccountBalance2020and2021=details['sec16h']
		USINRExchangeRateQ4=details['sec17a']
		USINRExchangeRateQ1=details['sec17b']
		USINRExchangeRate2019and2020=details['sec17c']
		USINRExchangeRate2020and2021=details['sec17d']
		Q11=details['part1a']
		Q12=details['part1b']
		Q13=details['part1c']
		Q2=details['part2']
		Q31=details['part3a']
		Q32=details['part2a']
		Q4=details['part3a']

		GVAtBasicPricesAtConstantPricesAAQ4=details['sec2e']
		GVAAtBasicPricesAtConstantPricesAAQ1=details['sec2f']
		GVAAtBasicPricesAtConstantPricesAA2019and2020=details['sec2g']
		GVAAtBasicPricesAtConstantPricesAA2020and2021=details['sec2h']
		GVAAtBasicPricesAtConstantPricesIQ4=details['sec2i']
		GVAAtBasicPricesAtConstantPricesIQ1=details['sec2j']
		GVAAtBasicPricesAtConstantPricesI2019and2020=details['sec2k']
		GVAAtBasicPricesAtConstantPricesI2020and2021=details['sec2l']
		GVAAtBasicPricesAtConstantPricesSQ4=details['sec2m']
		GVAAtBasicPricesAtConstantPricesSQ1=details['sec2n']
		GVAAtBasicPricesAtConstantPricesS2019and2020=details['sec2o']
		GVAAtBasicPricesAtConstantPricesS2020and2021=details['sec2p']

		MerchandiseExportUSDQ4=details['sec13e']
		MerchandiseExportUSDQ1=details['sec13f']
		MerchandiseExportUSD2019and2020=details['sec13g']
		MerchandiseExportUSD2020and2021=details['sec13h']
		MerchandiseExportGQ4=details['sec13i']
		MerchandiseExportGQ1=details['sec13j']
		MerchandiseExportG2019and2020=details['sec13k']
		MerchandiseExportG2020and2021=details['sec13l']

		MerchandiseImportUSDQ4=details['sec14e']
		MerchandiseImportUSDQ1=details['sec14f']
		MerchandiseImportUSD2019and2020=details['sec14g']
		MerchandiseImportUSD2020and2021=details['sec14h']
		MerchandiseImportGQ4=details['sec14i']
		MerchandiseImportGQ1=details['sec14j']
		MerchandiseImportG2019and2020=details['sec14k']
		MerchandiseImportG2020and2021=details['sec14l']

		CurrentAccountBalanceUSDQ4=details['sec16e']
		CurrentAccountBalanceUSDQ1=details['sec16f']
		CurrentAccountBalanceUSD2019and2020=details['sec16g']
		CurrentAccountBalanceUSD2020and2021=details['sec16h']
		CurrentAccountBalanceGDPQ4=details['sec16i']
		CurrentAccountBalanceGDPQ1=details['sec16j']
		CurrentAccountBalanceGDP2019and2020=details['sec16k']
		CurrentAccountBalanceGDP2020and2021=details['sec16l']


		files=request.files.getlist("files")
		file1=files[0]
		file2=files[1]
		# kk=[]
		# for file in files:
		# 	kk.append(file.filename.read())
		# filename1=kk
		# filename2=kk
		filename1=file1.read()
		filename2=file2.read()
        # filename2=file2.read()

		cur=mysql.connection.cursor()
		x = cur.execute("SELECT * FROM eco WHERE Email = (%s)",(Email,))
		if int(x)>0:
			return 'Name already taken'
		else:
			
			field_names = [i[0] for i in cur.description]
			print(len(field_names))	
			sql="INSERT INTO eco ( NameAndDesignation, CompanyName, Email, Mobile, GDPGrowthRateAtMarketPricesQ4, GDPGrowthRateAtMarketPricesQ1, GDPGrowthRateAtMarketPrices2019and2020, GDPGrowthRateAtMarketPrices2020and2020, GVAAtBasicPricesAtConstantPricesQ4, GVAAtBasicPricesAtConstantPricesQ1, GVAAtBasicPricesAtConstantPrices2019and2020, GVAAtBasicPricesAtConstantPrices2020and2021, GVAtBasicPricesAtConstantPricesAAQ4, GVAAtBasicPricesAtConstantPricesAAQ1, GVAAtBasicPricesAtConstantPricesAA2019and2020, GVAAtBasicPricesAtConstantPricesAA2020and2021, GVAAtBasicPricesAtConstantPricesIQ4, GVAAtBasicPricesAtConstantPricesIQ1, GVAAtBasicPricesAtConstantPricesI2019and2020, GVAAtBasicPricesAtConstantPricesI2020and2021, GVAAtBasicPricesAtConstantPricesSQ4, GVAAtBasicPricesAtConstantPricesSQ1, GVAAtBasicPricesAtConstantPricesS2019and2020, GVAAtBasicPricesAtConstantPricesS2020and2021, GrossDomesticSavingQ4, GrossDomesticSavingQ1, GrossDomesticSaving2019And2020, GrossDomesticSaving2020and2021, GrossFixedCapitalFormationQ4, GrossFixedCapitalFormationQ1, GrossFixedCapitalFormation2019and2020, GrossFixedCapitalFormation2020and2021, FiscalDeficitQ4, FiscalDeficitQ1, FiscalDeficit2019and2020, FiscalDeficit2020and2021, GrowthInIIPQ4, GrowthInIIPQ1, GrowthInIIP2019and2020, GrowthInIIP2020and21, WPIAllCommoditiesInflationRateQ4, WPIAllCommoditiesInflationRateQ1, WPIAllCommoditiesInflationRate2019and2020, WPIAllCommoditiesInflationRate2020and2021, CPICombinedNewInflationRateQ4, CPICombinedNewInflationRateQ1, CPICombinedNewInflationRate2019and2020, CPICombinedNewInflationrate2020and2021, PrimeLendingRateQ4, PrimeLendingRateQ1, PrimeLendingRate2019and2020, PrimeLendingRate2020and2021, MoneySupplyGrowthQ4, MoneySupplyGrowthQ1, MoneySupplyGrowth2019and2020, MoneySupplyGrowth2020and2021, BankCreditGrowthQ4, BankCreditGrowthQ1, BankCreditGrowth2019and2020, BankCreditGrowth2020and2021, RepoRateQ4, RepoRateQ1, RepoRate2019and2020, RepoRate2020and2021, MerchandiseExportUSDQ4, MerchandiseExportUSDQ1, MerchandiseExportUSD2019and2020, MerchandiseExportUSD2020and2021, MerchandiseExportGQ4, MerchandiseExportGQ1, MerchandiseExportG2019and2020, MerchandiseExportG2020and2021, MerchandiseImportUSDQ4, MerchandiseImportUSDQ1, MerchandiseImportUSD2019and2020, MerchandiseImportUSD2020and2021, MerchandiseImportGQ4, MerchandiseImportGQ1, MerchandiseImportG2019and2020, MerchandiseImportG2020and2021, TradeBalanceQ4, TradeBalanceQ1, TradeBalance2019and2020, TradeBalance2020and2021, CurrentAccountBalanceUSDQ4, CurrentAccountBalanceUSDQ1, CurrentAccountBalanceUSD2019and2020, CurrentAccountBalanceUSD2020and2021, CurrentAccountBalanceGDPQ4, CurrentAccountBalanceGDPQ1, CurrentAccountBalanceGDP2019and2020, CurrentAccountBalanceGDP2020and2021, USINRExchangeRateQ4, USINRExchangeRateQ1, USINRExchangeRate2019and2020, USINRExchangeRate2020and2021, Q11, Q12, Q13, Q2, Q31, Q32, Q4,doc1,doc2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			val=(NameAndDesignation, CompanyName, Email, Mobile, GDPGrowthRateAtMarketPricesQ4, GDPGrowthRateAtMarketPricesQ1, GDPGrowthRateAtMarketPrices2019and2020, GDPGrowthRateAtMarketPrices2020and2020, GVAAtBasicPricesAtConstantPricesQ4, GVAAtBasicPricesAtConstantPricesQ1, GVAAtBasicPricesAtConstantPrices2019and2020, GVAAtBasicPricesAtConstantPrices2020and2021, GVAtBasicPricesAtConstantPricesAAQ4, GVAAtBasicPricesAtConstantPricesAAQ1, GVAAtBasicPricesAtConstantPricesAA2019and2020, GVAAtBasicPricesAtConstantPricesAA2020and2021, GVAAtBasicPricesAtConstantPricesIQ4, GVAAtBasicPricesAtConstantPricesIQ1, GVAAtBasicPricesAtConstantPricesI2019and2020, GVAAtBasicPricesAtConstantPricesI2020and2021, GVAAtBasicPricesAtConstantPricesSQ4, GVAAtBasicPricesAtConstantPricesSQ1, GVAAtBasicPricesAtConstantPricesS2019and2020, GVAAtBasicPricesAtConstantPricesS2020and2021, GrossDomesticSavingQ4, GrossDomesticSavingQ1, GrossDomesticSaving2019And2020, GrossDomesticSaving2020and2021, GrossFixedCapitalFormationQ4, GrossFixedCapitalFormationQ1, GrossFixedCapitalFormation2019and2020, GrossFixedCapitalFormation2020and2021, FiscalDeficitQ4, FiscalDeficitQ1, FiscalDeficit2019and2020, FiscalDeficit2020and2021, GrowthInIIPQ4, GrowthInIIPQ1, GrowthInIIP2019and2020, GrowthInIIP2020and21, WPIAllCommoditiesInflationRateQ4, WPIAllCommoditiesInflationRateQ1, WPIAllCommoditiesInflationRate2019and2020, WPIAllCommoditiesInflationRate2020and2021, CPICombinedNewInflationRateQ4, CPICombinedNewInflationRateQ1, CPICombinedNewInflationRate2019and2020, CPICombinedNewInflationrate2020and2021, PrimeLendingRateQ4, PrimeLendingRateQ1, PrimeLendingRate2019and2020, PrimeLendingRate2020and2021, MoneySupplyGrowthQ4, MoneySupplyGrowthQ1, MoneySupplyGrowth2019and2020, MoneySupplyGrowth2020and2021, BankCreditGrowthQ4, BankCreditGrowthQ1, BankCreditGrowth2019and2020, BankCreditGrowth2020and2021, RepoRateQ4, RepoRateQ1, RepoRate2019and2020, RepoRate2020and2021, MerchandiseExportUSDQ4, MerchandiseExportUSDQ1, MerchandiseExportUSD2019and2020, MerchandiseExportUSD2020and2021, MerchandiseExportGQ4, MerchandiseExportGQ1, MerchandiseExportG2019and2020, MerchandiseExportG2020and2021, MerchandiseImportUSDQ4, MerchandiseImportUSDQ1, MerchandiseImportUSD2019and2020, MerchandiseImportUSD2020and2021, MerchandiseImportGQ4, MerchandiseImportGQ1, MerchandiseImportG2019and2020, MerchandiseImportG2020and2021, TradeBalanceQ4, TradeBalanceQ1, TradeBalance2019and2020, TradeBalance2020and2021, CurrentAccountBalanceUSDQ4, CurrentAccountBalanceUSDQ1, CurrentAccountBalanceUSD2019and2020, CurrentAccountBalanceUSD2020and2021, CurrentAccountBalanceGDPQ4, CurrentAccountBalanceGDPQ1, CurrentAccountBalanceGDP2019and2020, CurrentAccountBalanceGDP2020and2021, USINRExchangeRateQ4, USINRExchangeRateQ1, USINRExchangeRate2019and2020, USINRExchangeRate2020and2021, Q11, Q12, Q13, Q2, Q31, Q32, Q4,filename1,filename2)
			cur.execute(sql, val)
			mysql.connection.commit()
			cur.close()
			return 'sucess'	
	return render_template('index.html')

@app.route("/datatable",methods=['GET','POST'])
def datatable():
	mycursor=mysql.connection.cursor()
	mycursor=mysql.connection.cursor()
	mycursor.execute("SELECT id,NameAndDesignation,CompanyName,Email,Mobile,doc1,doc2 FROM eco")
	x=mycursor.fetchall()

	selected_data = request.args.get('type')

	if (selected_data) :
		mycursor.execute("SELECT * FROM eco WHERE id='"+selected_data+"'")
		mydata=mycursor.fetchall()
		field_names = [i[0] for i in mycursor.description]

		#mylist=[]

		# for i in mydata:
		# 	for j in range(len(i)):
		# 		if i[j]==selected_data:
		# 			mylist.append(i)
		return 	render_template('data.html',posts=mydata[0],field_names = field_names)

				

	return render_template('d.html',posts=x)

@app.route("/datatable",methods=['GET','POST'])
def download():
	return 'welcome'


if __name__ == '__main__':
    app.run(debug=True)