from loader import dp
from .chanel import ChannelMiddleware

if __name__=="middleware":
    dp.middleware.setup(ChannelMiddleware())

