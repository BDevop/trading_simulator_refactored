# Dictionary for each strategy in the trading simulation. Each system has a unique trading expectancy.
strategies = {
    "mean reversion":
        {
            "win rate": 38,
            "loss rate": 62,
            "expectancy": 0.61,
            "numbers": [-1, 8, -2, -1, 10, 7, 6, -1, -2, 6, -1, -1, 8, 7, 6, 5, 1, -1, -1, -1, -1, -1, 8, 10, 8, 6, 6,
                        3, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, 10, 10, 10, 7, 6, 5, -1, -1, -1, -1, -1, -1, -1, -1,
                        -1, -1, -1, -5, -1, -1, -1, -2, -2, -4, 8, 8, 6, 6, 6, 5, 4, 3, -1, -1, -1, -1, -1, -1, -1, -1,
                        -1, -1, -1, -1, 10, 7, 6, 5, -1, -1, -1, -1, -1, -2, -2, -3, 10, 10, 4, -1, -2, 7]
        },
    "breakout":
        {
            "win rate": 57,
            "loss rate": 43,
            "expectancy": 0.52,
            "numbers": [5, 10, 4, 2, 1, 4, 4, 5, 5, 1, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 5, 2, 4, 4, 3, 3, 3, 3, 3, 3,
                        3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1,
                        -1, -1, -6, -4, -2, -2, -2, -2, -10, -5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2,
                        -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, 1, -5]
        },
    "ipo":
        {
            "win rate": 63,
            "loss rate": 37,
            "expectancy": 0.76,
            "numbers": [1, 2, 5, 5, 3, 2, 4, 4, 4, -5, 4, -3, 3, 2, 5, -2, 3, 3, 3, 3, 3, 3, 1, 2, 1, 4, -3, 2, 2, 2, 2,
                        2, 2, 2, -5, 2, 2, 2, 1, 1, 3, 2, -5, 1, 1, 1, 1, 1, 1, -2, -1, 3, 1, 1, 1, 1, -3, -3, -3, -1,
                        -1, -1, 1, 1, -1, 2, 2, 1, -1, -1, -3, -5, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, 2, 3, 3, -2,
                        4, -2, -2, 5, 2, -2, -2, -2, 1, 1, -3, -3, -5, 5]
        },
    "trend following":
        {
            "win rate": 56,
            "loss rate": 44,
            "expectancy": 0.44,
            "numbers": [5, 2, 5, 1, 1, 1, 2, 4, 4, 2, 4, 4, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -3,
                        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -3, -1, -2, -2, -2, -2,
                        -2, -2, -2, -2, -5, -2, -2, -2, -2, -2, -3, -3, -5, -3]
        },
    "good news":
        {
            "win rate": 43,
            "loss rate": 57,
            "expectancy": 0.50,
            "numbers": [10, 8, 8, 8, 8, 7, 7, 7, 5, 5, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                        3, 3, 3, 2, -1, -1, 2, 2, 2, 2, 2, 2, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,
                        -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -1, -4]
        },
    "moving average":
        {
            "win rate": 56,
            "loss rate": 44,
            "expectancy": 0.64,
            "numbers": [10, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1,
                        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2,
                        -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -5, -5]
        },
    "contraction":
        {
            "win rate": 50,
            "loss rate": 50,
            "expectancy": 0.30,
            "numbers": [3, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1,
                        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2,
                        -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -2]
        },
    "delta neutral":
        {
            "win rate": 62,
            "loss rate": 38,
            "expectancy": 0.86,
            "numbers": [3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, -1, -1, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1,
                        -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -2, -2, -2, -2,
                        -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, 1, -5]
        },
    "canslim":
        {
            "win rate": 60,
            "loss rate": 40,
            "expectancy": 0.54,
            "numbers": [10, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -5, -1, -1, -1,
                        -5, -1, -1, -1, -3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -5, -2, -2, -2, -2,
                        -2, -2, -2, -2, -2, -2, -5, -3, -3, -5, -3, -10, -5]
        },
    "macro":
        {
            "win rate": 49,
            "loss rate": 51,
            "expectancy": 0.44,
            "numbers": [5, 5, 4, 4, 3, 3, 3, 8, 4, 4, 4, 6, 15, 3, 8, 3, 3, 10, 3, 3, 3, 3, 5, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 8, 2, 2, 10, 1, 1, 1, 5, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, 1,
                        -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,
                        -2, -2, -2, -2, -2, -2, -5, -2, -2, -4, -2, -3, -5, -3, -3, -10, -1]
        }
}

ticker = ["MMM", "AOS", "ABT", "ABBV", "ACN", "ATVI", "ADM", "ADBE", "ADP", "AAP", "AES", "GOOG", "MO", "AMZN",
          "AMCR", "AMD", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "CDNS", "CZR", "CPT", "CPB", "COF",
          "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CDAY", "CMG",
          "DOW", "DTE", "DUK", "DD", "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "ELV", "LLY", "EMR",
          "ENPH", "ETR", "EOG", "EPAM", "GL", "GS", "HAL", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE",
          "HLT", "HOLX", "HON", "HRL", "LEN", "LNC", "LIN", "LYV", "LKQ", "REGN", "RF", "RSG", "RMD", "RHI", "ROK",
          "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SBNY",
          "SPG", "SWKS", "SNA", "SEDG", "SO", "LUV", "SWK", "SBUX", "STT", "STLD", "STE", "SYK", "SIVB", "SYF",
          "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TRGP", "TGT", "TEL", "TDY", "TFX", "TER", "TSLA", "TXN",
          "TXT", "KO", "EL", "HD", "IPG", "SJM", "MOS", "TRV", "TMO", "TJX", "TSCO", "TT", "TDG", "TRMB", "TFC",
          "TYL", "TSN", "USB"]
