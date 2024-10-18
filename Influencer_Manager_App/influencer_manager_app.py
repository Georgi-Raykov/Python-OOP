from Influencer_Manager_App.campaigns.high_budget_campaign import HighBudgetCampaign
from Influencer_Manager_App.campaigns.low_budget_campaign import LowBudgetCampaign
from Influencer_Manager_App.influencers.premium_influencer import PremiumInfluencer
from Influencer_Manager_App.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    def __init__(self):

        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type, username, followers, engagement_rate):

        valid_type_influencer = {'PremiumInfluencer': PremiumInfluencer, 'StandardInfluencer': StandardInfluencer}

        if influencer_type not in valid_type_influencer:
            return f'{influencer_type} is not an allowed influencer type.'
        for influencer in self.influencers:
            if influencer.username == username:
                return f'{username} is already registered.'

        influencer = valid_type_influencer[influencer_type](username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f'{username} is successfully registered as a {influencer_type}.'

    def create_campaign(self, campaign_type, campaign_id, brand, required_engagement):

        valid_campaigns = {'HighBudgetCampaign': HighBudgetCampaign, 'LowBudgetCampaign': LowBudgetCampaign}
        if campaign_type not in valid_campaigns:
            return f'{campaign_type} is not a valid campaign type.'
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f'Campaign ID {campaign_id} has already been created.'
        campaign = valid_campaigns[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f'Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}.'

    def participate_in_campaign(self, influencer_username, campaign_id):
        influencer = self.__find_influencer_by_username(influencer_username)
        campaign = self.__find_campaign_by_id(campaign_id)

        if not influencer:
            return f'Influencer {influencer_username} not found.'
        if not campaign:
            return f'Campaign with ID {campaign_id} not found.'
        if not campaign.check_eligibility(influencer.engagement_rate):
            return f'Influencer {influencer_username} does not meet the eligibility criteria for the campaign ' \
                   f'with ID {campaign_id}'
        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f'Influencer {influencer_username} has successfully participated in the campaign with ' \
                   f'ID {campaign_id}'

    def calculate_total_reached_followers(self):

        total_followers = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_fellows = influencer.reached_followers(campaign.__class__.__name__)
                if campaign not in total_followers:
                    total_followers[campaign] = 0
                total_followers[campaign] += reached_fellows

        return total_followers

    def influencer_campaign_report(self, username):

        influencer = self.__find_influencer_by_username(username)
        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):

        total_reached_followers = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        result = ['$$ Campaign Statistics $$', ]
        for campaign in sorted_campaigns:
            result.append(f'* Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, '
                          f'Total budget: {campaign.budget:.2f}, Total reached followers: '
                          f'{total_reached_followers.get(campaign)}')
        return '\n'.join(result)

    def __find_campaign_by_id(self, id):

        for campaign in self.campaigns:
            if campaign.campaign_id == id:
                return campaign
        return None

    def __find_influencer_by_username(self, username):

        for influencer in self.influencers:
            if influencer.username == username:
                return influencer
        return None
