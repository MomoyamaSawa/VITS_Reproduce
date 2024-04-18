import json


class ReproduceParams:
    """
    复现的时候的额外参数
    """

    def __init__(self):
        with open("params.json", "r", encoding="utf-8") as f:
            params = json.load(f)
        self.model_dir = params["model_dir"]
