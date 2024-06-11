from fastapi import FastAPI
from openData import faliticies, facility, statistic
from datetime import date
from utils import convert_to_timestamp

app = FastAPI()


@app.get('/')
async def test():
    return {"response": "success."}

@app.get('/apiv1/falicities')
async def get_facilities(page, country=None, extent=None, created_from:date =None, latest_to:date=None):

    
    result = faliticies(
        page, country, 
        extent, 
        convert_to_timestamp(created_from), 
        convert_to_timestamp(latest_to))

    return result
    # return {
    #     "from": convert_to_timestamp(created_from),
    #     "to":  convert_to_timestamp(latest_to)
    # }

@app.get('/apiv1/falicities/statistic')
async def get_statistic(country=None, extent=None, created_from=None, latest_to=None):

    result = statistic(country, extent, created_from, latest_to)

    return result


@app.get('/apiv1/falicities/{osm_type}/{osm_id}')
async def get_facility(osm_type, osm_id):

    result = facility(osm_type, osm_id)

    return result