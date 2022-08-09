
from data.models import Rate
from django.db.models import Avg

def avg (week_ago,mydate):
    
    atten=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('attention'))
    behav=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('behavior'))
    interaction=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('interaction'))
    communiction_skills=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('communiction_skills'))
    leadership_skills=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('leadership_skills'))
    team_skills=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('team_skills'))
    logical_thinking=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('logical_thinking'))
    critical_thinking=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('critical_thinking'))
    creative_thinking=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('creative_thinking'))
    proplem_solving=Rate.objects.filter(date__range=[week_ago,mydate]).aggregate(Avg('proplem_solving'))
    
    return atten,behav,interaction,communiction_skills,leadership_skills,team_skills,logical_thinking,critical_thinking,creative_thinking,proplem_solving