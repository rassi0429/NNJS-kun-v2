import asyncio
from pathlib import Path
import re

import sys

from boilerplate import API
from novelai_api.ImagePreset import ImageModel,ImageSampler, ImagePreset, ImageResolution, UCPreset


async def generateImage(prompt: str = "1girl"):
    d = Path("results")
    d.mkdir(exist_ok=True)

    print(prompt)

    async with API() as api_handler:
        api = api_handler.api

        preset = ImagePreset()
        preset.resolution = ImageResolution.Normal_Portrait_v3
        preset.uc_preset = UCPreset.Preset_None
        preset.n_samples = 1
        preset.steps = 28
        preset.uc = "lowres, {bad}, error, fewer, extra, missing, worst quality, jpeg artifacts, bad quality, watermark, unfinished, displeasing, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]"
        preset.noise_schedule = "native"
        preset.cfg_rescale = 1
        preset.scale = 6
        preset.sampler = ImageSampler.k_euler

        # multiple images
        # preset.n_samples = 4
        if(api is None):
            print("api.high_level is None")
            return
        
        if("v2" in prompt):
            print("v2")
            prompt = re.sub(r"v2", "", prompt)
            async for _, img in api.high_level.generate_image(prompt, ImageModel.Anime_v2, preset):
                (d / f"image.png").write_bytes(img)
            return

        prompt = re.sub(r"v3", "", prompt)
        print("v3")
        async for _, img in api.high_level.generate_image(prompt, ImageModel.Anime_v3, preset):
            (d / f"image.png").write_bytes(img)

if __name__ == "__main__":
    # get arguments from std input
    args = sys.argv[1:]
    # join arguments with spaces
    prompt = ",".join(args)
    asyncio.run(generateImage(prompt = prompt))
    