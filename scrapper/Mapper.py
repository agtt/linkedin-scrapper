class Mapper:

    def profileMapper(self, data):
        data = data["included"]
        m = {}
        m['profile'] = {}
        m['skills'] = []
        m['educations'] = []
        m['languages'] = []
        m['experiences'] = []
        m['certifications'] = []
        m['projects'] = []
        for a in data:
            type = a['$type']
            if type == 'com.linkedin.voyager.identity.profile.Profile':
                """ Main Profile Data """
                m['profile'] = a
            if type == 'com.linkedin.voyager.identity.profile.Skill':
                """ Get Skills """
                m['skills'].append(a)
            if type == 'com.linkedin.voyager.identity.profile.Education':
                """ Get Educations """
                m['educations'].append(a)
            if type == 'com.linkedin.voyager.identity.profile.Language':
                """ Get Languages """
                m['languages'].append(a)

            if type == 'com.linkedin.voyager.identity.profile.Position':
                """ Get Experience """
                m['experiences'].append(a)
            if type == 'com.linkedin.voyager.identity.shared.MiniProfile':
                """ Get Images """
                m['pictures'] = {'images': a['picture']['artifacts'], 'rootUrl': a['picture']['rootUrl'],
                                 'backgroundimage': a['backgroundImage'], 'publicIdentifier': a['publicIdentifier']}
            if type == 'com.linkedin.voyager.identity.profile.Certification':
                """ Get Certification """
                m['certifications'].append(a)
            if type == 'com.linkedin.voyager.identity.profile.Project':
                """ Get Projects """
                m['projects'].append(a)

        return m

    def searchMapper(self, data):
        data = data['included']
        profiles = []
        for p in data:
            if p['$type'] == 'com.linkedin.voyager.identity.shared.MiniProfile':
                profiles.append({'firstname': p['firstName'], 'lastname': p['lastName'], 'occupation': p['occupation'],
                                 'publicIdentifier': p['publicIdentifier'], 'trackingId': p['trackingId']})
        return profiles
