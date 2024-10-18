from Influencer_Manager_App.campaigns.base_campaign import BaseCampaign
from Influencer_Manager_App.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.85

    def __init__(self, username, followers, engagement_rate):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * PremiumInfluencer.PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type):

        if campaign_type == 'HighBudgetCampaign':

            return self.followers * self.engagement_rate * 1.5
        elif campaign_type == 'LowBudgetCampaign':
            return self.followers * self.engagement_rate * 0.8
