class BrazeMain():
    def __init__(self):
        pass

    async def post(self, **kwargs):
        print("\nExecuting Braze api...")
        # headers = {
        #     "Authorization": os.getenv("BRAZE_REST_API_KEY")
        # }
        # header = [
        #     "external_id",
        #     "is_apppush_target"
        # ]
        #
        # data = [
        #     {
        #         header[i]: int(row[i]) if i == 0 else row[i]  # 563957
        #         if row[i] == 'y' else 'n'
        #         for i in range(0, len(row))
        #     } for row in data
        # ]
        # data = [
        #     {
        #         **item,
        #         'is_push_target': None
        #     } for item in data
        # ]
        # if len(data) != 0:
        #     print("Data: ", data, len(data))
        # else:
        #     return
        #
        # url = os.getenv("BRAZE_INSTANCE")
        # Todo: Async POST
        # try:
        #     async with session.post(
        #             url,
        #             headers=headers,
        #             json={"attributes": data},
        #             ssl=False,
        #     ) as response:
        #         # 응답 처리 로직
        #         # res = response.json()
        #         # print("\nBraze Res:", res)
        #         await asyncio.sleep(0.01)
        # except aiohttp.ClientConnectorError as e:
        #     raise f"Connection Error: {str(e)}"
        return "End Extract"

    async def transform(self, **kwargs):

        return "End Transform"
