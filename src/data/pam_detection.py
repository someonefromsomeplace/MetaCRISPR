class PAMDetector:
    def detect(self, processed):
        sequence = processed["validated_sequence"]

        # mock PAM detection (NGG-like simulation)
        sites = []
        for i in range(len(sequence) - 3):
            if sequence[i:i+2] == "GG":
                sites.append(i)

        return sites
