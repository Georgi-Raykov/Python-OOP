from Influencer_Manager_App.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, 2500.0, required_engagement)

    def check_eligibility(self, engagement_rate):
        return engagement_rate >= self.required_engagement * 0.9
