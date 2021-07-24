
#  STORM json parts-> get png -> save file+
import json
import asyncio
import requests
import os

async def divide():
    for name,url in json.load(open('assets/json/data.json')).items():
        yield name,url

async def getPng(save_name,name,url):
    r = requests.get(url)
    cart=await makeLegend(save_name,name)
    legend.update(cart)
    with open("assets/img/"+str(save_name)+".png", "wb") as f:
        f.write(r.content)
    await saveLegend(legend)

async def saveLegend(legend):
    with open("assets/legend/legend.json", "w") as outfile:
        json.dump(legend,indent=4,fp=outfile)    
async def makeLegend(save_name,name):
    cart={}
    cart[save_name]=name
    return cart

async def main():
    count=1
    async for i,j in divide():
        await getPng(count,i,j)
        count+=1

legend={}
asyncio.run(main())