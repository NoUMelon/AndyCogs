from .giveaway import Giveaways

def setup(bot):
    bot.add_cog(Giveaways(bot))