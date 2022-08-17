from data.models import Rate, Student
from django.db.models import Avg

def avg (week_ago,mydate,pk,pk1):
    
    attention=Rate.objects.filter(student=pk,subject=pk1,date__range=[week_ago,mydate]).aggregate(Avg('attention'))
    behavior=Rate.objects.filter(student=pk,subject=pk1,date__range=[week_ago,mydate]).aggregate(Avg('behavior'))
    interaction=Rate.objects.filter(student=pk,subject=pk1,date__range=[week_ago,mydate]).aggregate(Avg('interaction'))
    
    communiction_skills=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('communiction_skills'))
    leadership_skills=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('leadership_skills'))
    team_skills=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('team_skills'))
    logical_thinking=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('logical_thinking'))
    critical_thinking=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('critical_thinking'))
    creative_thinking=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('creative_thinking'))
    proplem_solving=Rate.objects.filter(student=pk,subject=pk1, date__range=[week_ago,mydate]).aggregate(Avg('proplem_solving'))
    if (attention['attention__avg']):
        return [{"attention":round(attention['attention__avg']),
           "behavior":round(behavior['behavior__avg']),
            "interaction":round(interaction['interaction__avg']),
            "communiction_skills":round(communiction_skills['communiction_skills__avg']),
            "leadership_skills":round(leadership_skills['leadership_skills__avg']),
            "team_skills":round(team_skills['team_skills__avg']),
            "logical_thinking":round(logical_thinking['logical_thinking__avg']),
             "critical_thinking":round(critical_thinking['critical_thinking__avg']),
           "creative_thinking":round(creative_thinking['creative_thinking__avg']),
             "proplem_solving":round(proplem_solving['proplem_solving__avg'])
               }]
    else:return 0