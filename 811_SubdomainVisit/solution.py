class Solution:
    def subdomainVisits(self, cpdomains):
        visits = {}

        for pair in cpdomains:
            num, domain = pair.split()
            num = int(num)

            subdomain = ""
            for sub in reversed(domain.split('.')):
                subdomain = sub + subdomain

                if subdomain not in visits:
                    visits[subdomain] = 0
                visits[subdomain] += num

                subdomain = '.' + subdomain
        
        return [str(visits[i]) + " " + i for i in visits.keys()]