
class Stats_service:

    def Get_overall_stats(self, coach_obj):
        
        human_matches = coach_obj.matches['Human']

        for match in human_matches:
            print(match.race_opp)