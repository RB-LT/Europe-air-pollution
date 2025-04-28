import cdsapi

#You need a file in C:\Users\USERNAME called .cdsapirc
#with the bellow contents (get key from Copernicus/ECMWF)

#url: https://ads.atmosphere.copernicus.eu/api
#key: ********-****-****-****-***********

# SOME OPTION COMBINATIONS ARE NOT POSSIBLE CHECK BELLOW IF POSSIBLE
# https://ads.atmosphere.copernicus.eu/datasets/cams-europe-air-quality-reanalyses?tab=download

# YOU CAN SELECT MULTIPLE OPTIONS
# UNCOMMENT TO ENABLE MULTIPLE

dataset = "cams-europe-air-quality-reanalyses"
request = {
    "variable": [
        # "ammonia",
        # "carbon_monoxide",
        # "formaldehyde",
        # "glyoxal",
        "nitrogen_dioxide",
        "nitrogen_monoxide",
        # "non_methane_vocs",
        # "ozone",
        # "particulate_matter_2.5um",
        # "residential_elementary_carbon",
        # "secondary_inorganic_aerosol",
        # "total_elementary_carbon",
        # "pm2.5_total_organic_matter",
        "particulate_matter_10um",
        # "dust",
        "pm10_sea_salt_dry",
        "pm10_wildfires",
        # "peroxyacyl_nitrates",
        # "sulphur_dioxide"
    ],
    "model": [
        # "ensemble",
        "chimere",
        # "emep",
        # "lotos",
        # "match",
        # "minni",
        # "mocage",
        # "monarch",
        # "silam",
        # "euradim",
        # "dehm",
        # "gemaq"
    ],
    "level": [
        # "0",
        "50",
        # "100",#CHECK
        # "250",
        # "500",
        # "750",#CHECK
        # "1000",
        # "2000",
        # "3000",
        # "5000"
    ],
    "type": [
        "validated_reanalysis",
        # "interim_reanalysis"
    ],
    "year": [
        # "2013",
        # "2014",
        # "2015",
        # "2016",
        # "2017",
        "2018",
        # "2019",
        # "2020",
        # "2021",
        # "2022",
        # "2023"
    ],
    "month": [
        # "01",
        # "02",
        # "03",
        # "04",
        # "05",
        # "06",
        # "07",
        # "08",
        # "09",
        # "10",
        # "11",
        "12"
    ]
}

client = cdsapi.Client()
filename=str("temp.zip")
client.retrieve(dataset, request).download(filename)

