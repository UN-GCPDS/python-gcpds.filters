#  common average reference (CAR)
def CAR(subjects):
    SubjectsCAR = subjects
    fil = len(subjects)
    for l in range(0,fil): ## 9
        subject = subjects[l,0]
        fil = len(subject)
        SubjectCAR = subject
        for k in range(0, fil): ## 273
            Sample = subject[k,0]
            SampleCAR = Sample
            prom = np.mean(Sample,1)
            promedio = np.array(prom)
            prom_one = npmat.repmat(promedio,22,1)
            promedio = prom_one.T
            SampleCAR = Sample - promedio
            SubjectCAR[k,0] = SampleCAR ## Subject
        SubjectsCAR[l,0] = SubjectCAR
    return SubjectsCAR
