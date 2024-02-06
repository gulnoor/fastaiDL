import asyncio
from duckduckgo_search import DDGS
from duckduckgo_search.duckduckgo_search_async import AsyncDDGS
from fastai.data.block import DataBlock
import fastai.vision.all as fv
import fastcore.all as fc
from fastdownload import download_url
import skimage.io as io
import matplotlib.pyplot as plt


async def search():
    async with AsyncDDGS() as ddgs:
        image_gen = ddgs.images(keywords=("pacman"), max_results=10)
        imglist = fc.L(image_gen).itemgot("image")
        return imglist
   
# %%
async def main():
    path = fc.Path("images/pacman")
    path.mkdir(parents=True, exist_ok=True)
    fv.download_images(path, urls=search())
    b = DataBlock()

    print("foo")
    print("exit")


if __name__ == "__main__":
    asyncio.run(main())
