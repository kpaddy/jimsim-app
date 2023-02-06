import requests
pool_info_endpoint = "https://lifinity.io/api/poolinfo"
pool_info_endpoint_v2 = "https://lifinity.io/api/poolinfo-v2"

class TokenHistoryPriceProcessor( object ):
   def __init__(self ) -> None:
      conn_string = 'postgresql://{}:{}@{}/{}'.format( os.getenv("db_user") , os.getenv("db_pass"), os.getenv("db_host"), os.getenv("db_name"))
      self.db = create_engine(conn_string)
      self._conn = self.db.connect()

   def save_price_to_db(self, rows) :
      stmt = insert( DeFiTokenPrice, ).values(rows)    
      self._conn.execute(stmt)



def fetch_data( endpoint ):
   resp = requests.get(endpoint)
   data = resp.json()
   for t in data :
      print( t )

fetch_data( pool_info_endpoint )
fetch_data( pool_info_endpoint_v2 )

{'symbol': 'UXD-USDT', 'volume7Days': 0, 'volume7DaysX': 0, 'volume7DaysY': 0, 'volumeYesterDay': 0, 'volumeYesterDayX': 0, 'volumeYesterDayY': 0, 'fee': 5.9758281609962325e-05, 'netapr': -116.76230489129506, 'ca': -116.76236454181222, 'startDate': '2022/05/06', 'coinBalance': 1076941, 'pcBalance': 923143, 'liquidity': '$2.00', 'liquidityAmount': 2.00031162224976, 'pythPrice': 1.00021136, 'pythPcPrice': 1}

pool_list_v2 = {
    "SOL-USDC": {
        "amm": "86eq4kdBkUCHGdCC2SfcqGHRCBGhp2M89aCmuvvxaXsm",
        "poolMint": "FbQYjLEq1vNCszmxmxZDoFiy9fgyfdPxzt9Fu5zk5jJ4",
        "feeAccount": "FX5PBDb4nVTs4f9dSkUsj55rEYrCkBs9e7xZpDHqDeVM",
        "oracleMainAccount": "EPBJUVCmzvwkGPGcEuwKmXomfGt78Aozy6pj44x9xxDB",
        "oracleSubAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "oraclePcAccount": "CdgEC82BZAxFAJFpVPZ1RtnDr9AyH8KP9KygYhCb39eJ",
        "poolCoinTokenAccount": "6Nij2pGdpgd6EutLAtdRwQoHaKKxhdNBi4zoLgd9Yuaq",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "ELFYDkPYWBopH5Msm2cbA2ueByCXEKpzKWanv1kZC9L2",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "SOL-USDT": {
        "amm": "EiEAydLqSKFqRPpuwYoVxEJ6h9UZh9tsTaHgs4f8b8Z5",
        "poolMint": "2e6NAJy1qaKMq8PaswP2uzimMDvbr71Tbw38G6q9SNZ2",
        "feeAccount": "2EVZT2cFMvbqE9nSVidYVkrSouKfudcKG6R8AKiXoSY9",
        "oracleMainAccount": "EPBJUVCmzvwkGPGcEuwKmXomfGt78Aozy6pj44x9xxDB",
        "oracleSubAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "oraclePcAccount": "3ZDBff7jeQaksmGvmkRix36rU159EBDjYiPThvV8QVZM",
        "poolCoinTokenAccount": "GUicRosQyLJCYG8hjYcbiGKAVAmT1puQTVmJjFxJmdMK",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "D8F3PPxSuykAgyPPKwQdXDGGoRnUXzxowaheVJw5ATDC",
        "poolPcMint": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "stSOL-USDC": {
        "amm": "HPmjoycx8Vm99Tc9mUhRZWfJy4fsEZxVwhzP5nw7XeEy",
        "poolMint": "2bykZULRJwHikmUzDFvQLvoMZWMmbrJR1ivCAwtPuXpG",
        "feeAccount": "2kFxaaVnxWRHnVLjmy8DpaaNDPRVU6E9UefKs1P7Riu6",
        "oracleMainAccount": "EPBJUVCmzvwkGPGcEuwKmXomfGt78Aozy6pj44x9xxDB",
        "oracleSubAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "oraclePcAccount": "9gP2pFYs8GB7DzQ5QuB3muRyW8ct5vHttamiDfNhpj7E",
        "poolCoinTokenAccount": "35xntLJUTBzV8nSAPY2s1cdMdSNprccYhq7YSZae8gzy",
        "poolCoinMint": "7dHbWXmci3dT8UFYWYZweBLXgycu7Y3iL6trKn1Y7ARj",
        "poolPcTokenAccount": "AEyvfXM3pmQmAvijyWeGro25yrCXUWij5YZLhnK3sAKP",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "mSOL-USDC": {
        "amm": "HvtYZ3e8JPhy7rm6kvWVB2jJUddyytkLcwTMSSnB7T3U",
        "poolMint": "4CuuyBmdbYFUfXh2EHdJ7o2ZT246MR6xVU9vQD1yvDbx",
        "feeAccount": "2WbmNq2pbwYzpkgdxFdZjcw5nfVBhmTaUbatMui3pQes",
        "oracleMainAccount": "EPBJUVCmzvwkGPGcEuwKmXomfGt78Aozy6pj44x9xxDB",
        "oracleSubAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "oraclePcAccount": "9UfxaBfNPEBC4jyZCzXJrKR5dTJprevBUYtPWEZ56GRm",
        "poolCoinTokenAccount": "5z4wU1DidgndEk4oJPsKUDyQxRgZpVWrhwVnMAU6XTJE",
        "poolCoinMint": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
        "poolPcTokenAccount": "Dz6KvVqCBeiGXMEXyqQv81QHLoEdui1BYGY4RL7F6cwq",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    }
}
pool_list_v1 = {
    "SOL-USDC": {
        "amm": "amgK1WE8Cvae4mVdj4AhXSsknWsjaGgo1coYicasBnM",
        "poolMint": "3WzrkFYq4SayCrhBw8BgsPiTVKTDjyV6wRqP7HL9Eyyw",
        "feeAccount": "AD5DFr1AXMB9h6fw5KFtkEfwf7kYSAiaSueeu4NGrLKY",
        "configAccount": "2iT9h99mhDqetoZGNj7KKrqBnoDmFvAytGrnFYuR7MwN",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "5JLNs3VxLVVJt8CCVyRhjgTwey8WCaU3VeKcT7SJCzXQ",
        "poolCoinTokenAccount": "2uySTNgvGT2kwqpfgLiSgeBLR3wQyye1i1A2iQWoPiFr",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "32SjGNjesiCZgmZb4YxAGgjnym6jAvTWbqihR4CvvXkZ",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "SOL-USDT": {
        "amm": "2x8Bmv9wj2a4LxADBWKiLyGRgAosr8yJXuZyvS8adirK",
        "poolMint": "BRchiwrv9yCr4jAi6xF4epQdtNtmJH93rrerpHpMhK1Z",
        "feeAccount": "GFj8cNTP4mzWG7ywyJ35Ls2V8CbqDk3p4xNT1pAawoCh",
        "configAccount": "Hor7j9oYfNH6EJgmnXQRiQSahduR5p4bfKyCZaQUqNKd",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "GhMcWrkx5PG6XS1Dt61Sp5bCGtbWgoBKRtaV1ziVjnvA",
        "poolCoinTokenAccount": "5pH2DBMZg7y5bN4J3oLKRETGXyVYPJpeaCH6AkdAcxqp",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "7Cct2MJUwruQef5vQrP2bxYCNyVajJ3SiC1GYUmwmjUm",
        "poolPcMint": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "SOL-UXD": {
        "amm": "GjnY1NbZafYu6VSK2ELh5NRZs7udGAUR2KoAB7pYxJak",
        "poolMint": "E9e9UPZvzLCtPNWimJk8T7JDKX6hvHWGe2ZTY1848bQf",
        "feeAccount": "ZRfAnqPSnyY4USGnoeJTNrriqPfudm2a9811vYHYniQ",
        "configAccount": "3BUS8iaWzGjtCueoChEsu1N8Fh9QeQp8foJsU4tdKkJ7",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "6qyKHAbqFUGqukKDXK47f7ZFxfg3zsX3LYCaiTgwnCxk",
        "poolCoinTokenAccount": "4byV1TrowZopVezaBLL5cMbAaU3TZ5BQdtitHFWDBfuE",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "4JciXWsVimE9tqnmgQ8AjZqYZwiF6fx6zCxWf9PCrZ2n",
        "poolPcMint": "7kbnvuGBxxj8AG9qp8Scn56muWGaRaFqxg1FsRp3PaFT",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "SOL-PAI": {
        "amm": "E64HmCLED4nMMdHZrVTPL2FYCPEPZRJF8sViQeAuxygJ",
        "poolMint": "iin7tpvFQ1f3GSUuNcqxsFKNE8gHk3xCYs5Fm5UPh8T",
        "feeAccount": "5hw84YwNopuAJ2TcDGPPMiB1pGwhHprTaaqTiYJ6qDpT",
        "configAccount": "3rP1h4txRHZh2pt9DTXoWrvYRpWd7kyVf83fKUHTuYLG",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "3dQnwPvTgc6M2HmZqDYrTP4m2oiKAy3dwe3qJhqyf8nH",
        "poolCoinTokenAccount": "DQoV2vnbZ2jpmMQaYWWZraJuqXTWeqCoHBCmmkymi4C1",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "FGS1xT4neZEpA14DqFH9r5tHbK8d12BmNCA7sMQVrVdv",
        "poolPcMint": "Ea5SjE2Y6yvCeW5dYTn7PYMuW5ikXkvbGdcmSnXeaLjS",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "stSOL-USDC": {
        "amm": "2WGgMXSZQtLhUBQzXoavXTfirgGsJFVs2huCRSB4ukVP",
        "poolMint": "HfkJfTEVBv6xFDN2NGbsn3sxbooJDHDcfRoAT422P9Rq",
        "feeAccount": "jjjyK11wScEKmjqUCcGRD4kmfChUm8XJ7KhxzS4aUsi",
        "configAccount": "Ce4qSNPr6LaksUytdePUp7EQq6SbGDjoQWb2VvfewYwT",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "9gP2pFYs8GB7DzQ5QuB3muRyW8ct5vHttamiDfNhpj7E",
        "poolCoinTokenAccount": "8596RX9J4fXHKLQKrF9MCB8buq1jydhpUGjCSzgjnmbt",
        "poolCoinMint": "7dHbWXmci3dT8UFYWYZweBLXgycu7Y3iL6trKn1Y7ARj",
        "poolPcTokenAccount": "AjVCdqSFNzxYnyaKEHF3YHM7yBTkwVZynekJDBtXJ4Z",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "stSOL-UXD": {
        "amm": "CMu86zkJtcqYTBgKMf1fJWhcowQBVmysNsWthXZNZpYZ",
        "poolMint": "AFBYo7dFZzS18dKg965VVdoiV7cmSj9AX81uwCEYFyvA",
        "feeAccount": "tdTP4XEKYyfxTPg3EuRZbrZmm7p882u7BBWPaNahraP",
        "configAccount": "GVZZaF3YPRSkG8CB1hC4bGYrg6g7LEiWmPpKH4BE4b2n",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "tRCderESn7r9UARDATUxMesd282QjkpwM9pkmizFbWE",
        "poolCoinTokenAccount": "4QydTFxiZ4art8Fo67L4UnvGHWJSQAh6a1JXPuxk5aaT",
        "poolCoinMint": "7dHbWXmci3dT8UFYWYZweBLXgycu7Y3iL6trKn1Y7ARj",
        "poolPcTokenAccount": "C92rvQ4zXhYb3pHsN2dNnH5jW35UTFYbuZd1YDWzZhDc",
        "poolPcMint": "7kbnvuGBxxj8AG9qp8Scn56muWGaRaFqxg1FsRp3PaFT",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "mSOL-USDC": {
        "amm": "Ct5i81oqzw9Z2JnbNGjKUKExEaUJeDBBtWLRSkWD5DjR",
        "poolMint": "BKq1HN9expTKLvjkpnvcbHvsHukTUecdHyUZF7H2p2jr",
        "feeAccount": "Be7r4yNbZ2Qf61aXUPZVvHtcgXX5X6V7MYDoVuqhPSsy",
        "configAccount": "7dPSHYkBNvp1YBnaoXGcGZe2cJ3dUkKNWrYif69JCMur",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "9UfxaBfNPEBC4jyZCzXJrKR5dTJprevBUYtPWEZ56GRm",
        "poolCoinTokenAccount": "AymgLAHXAHLuZXqF5h8SxfmvwVQ4VykKhUJda87DUWZe",
        "poolCoinMint": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
        "poolPcTokenAccount": "Cr3wSVy5EAWzcQ7pDw4VEfADbNM65NNxpX6wxV1sxLWy",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "mSOL-UXD": {
        "amm": "3UpSTFAuRgCzhnjmkm6rPvzRNLb8PXSAR5h7Qdi8kJkd",
        "poolMint": "GDSANx8mvoeBgrx8hMoY8hGauCods6ARva2Vwtx6UjTR",
        "feeAccount": "DyFsGNHaBZew2HNVqu6nDxoJVrT2MM4rPKVGRqEBLLKZ",
        "configAccount": "5mVj5qg99sYaCMehDQYUYwKVDCWEeKv7WL4PoigWCw8y",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "EqqEnFJPMhAVftpsFzbBa4ByMMJgXBNiRkJC89ZK6UFL",
        "poolCoinTokenAccount": "2u4darckm8R24hZdYQEWDQwMRuQCh1x4zDtEZr74Kiue",
        "poolCoinMint": "mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So",
        "poolPcTokenAccount": "Ej6anT2VVx5MPSBdanfUSVELnssGJqfGSeitppMYh74R",
        "poolPcMint": "7kbnvuGBxxj8AG9qp8Scn56muWGaRaFqxg1FsRp3PaFT",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "SOL-UST": {
        "amm": "65E23qmpbcq3EynyxzSAk5PmAXv4NYmRb2jJiYDDRCaB",
        "poolMint": "4aUVFHRR3c3Zyzi4yeT4U38x1hsPWE8VstKWAXkpgE7g",
        "feeAccount": "Dyr7rzzrZbyHwHmx5YC4xcfzRJpuxDPmWu8BmwNzkAL4",
        "configAccount": "5CmmN7dYxsmP88dE1eATYJc1SjKQXhZFs1FeDSdq5s2C",
        "pythAccount": "H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
        "pythPcAccount": "H8DvrfSaRfUyP1Ytse1exGf7VSinLWtmKNNaBhA4as9P",
        "poolCoinTokenAccount": "AgiA6x7T6vR2J8ZPeBGizWruwhP6HBbpoW3Hg5jh2f2b",
        "poolCoinMint": "So11111111111111111111111111111111111111112",
        "poolPcTokenAccount": "3eM8HhW5XQeEmshqSvNSmrPmYuBKZpPXVVfzvqgYvJAv",
        "poolPcMint": "9vMJfxuKxXBoEa7rM12mYLMwTacLMLDJqHozw96WQL8i",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "BTC-USDC": {
        "amm": "HeH3s7B3a6nynim1rBGS6TRaYECgSNjt7Kp65mhW9P4k",
        "poolMint": "BzuTSoWFHrnRQvn4sr5ErPQyMaRB9g2rsbKCruGtcvMa",
        "feeAccount": "5HpNeHBBpg6x7fzTgbvP9UukQmDmvxbggwqo951BYkba",
        "configAccount": "HuLmRVTfYjNYYGBpPtJEk7JKkosbbPF4zzBHnf3TfyCn",
        "pythAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "pythPcAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "poolCoinTokenAccount": "FAFShq3gZYXWtk5EkeKPKcwSkz2rjfMDuD1i7KiYwjVM",
        "poolCoinMint": "9n4nbM75f5Ui33ZbPYXn59EwSgE8CGsHtAeTH5YFeJ9E",
        "poolPcTokenAccount": "3ReY1xscSAEV9Qg1NshkU4KRWQs33nu5JMg8AnoU7duG",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 8,
    },
    "ETH-USDC": {
        "amm": "E32Z6DYwJELMTrVJVchN8PWbyhSoC3bRorMb7Cw2R9Xz",
        "poolMint": "8FxRyaE8X6ENLmNbaBvgS6vMsN1GJ8J7CmKy8K8uN6wM",
        "feeAccount": "5yXQ399ti5rKMcRMAZvFUqAgKHUP55bvhoYWd9bVrnu9",
        "configAccount": "5JXrQpWAPNrvVN1R6Mz9MhA1EYUB948kceZjCxRzQzf5",
        "pythAccount": "JBu1AL4obBcCMqKBBxhpWCNUt136ijcuMZLFvTP7iWdB",
        "pythPcAccount": "JBu1AL4obBcCMqKBBxhpWCNUt136ijcuMZLFvTP7iWdB",
        "poolCoinTokenAccount": "BRFwAToCofwzP29jVGzb6VZ4AGpw867AE5VsXfMsmEGk",
        "poolCoinMint": "7vfCXTUXx5WJV5JADk17DUJ4ksgau7utNKj4b963voxs",
        "poolPcTokenAccount": "FDCjDSbFCVRVBsWkJWfgZ9x3Dizm1MJjtzYw3R2fxXRv",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 8,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 10,
    },
    "RAY-USDC": {
        "amm": "FcxHANr1dguexPZ2PoPGBajgiednXFMYHGGx4YMgedkM",
        "poolMint": "HUpvKUafPCMwhua6QtHXk1V8D6LZYyQmUKYPFZgRiiiX",
        "feeAccount": "DyR91PiiRopbdcizbjdXejodjxEeVSs4uCkyhL7wCvxw",
        "configAccount": "2EXv6K3cYDMXXKFfzGjqnjkbngUymnVwBoC4kwrCKwFy",
        "pythAccount": "AnLf8tVYCM816gmBjiy8n53eXKKEDydT5piYjjQDPgTB",
        "pythPcAccount": "AnLf8tVYCM816gmBjiy8n53eXKKEDydT5piYjjQDPgTB",
        "poolCoinTokenAccount": "BhG9r4CkTBRtpLtxA8Hd72vCkikqyVhiq8pFunZNERV8",
        "poolCoinMint": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R",
        "poolPcTokenAccount": "8HAVXU7bdS2SEkkrqFBdWPFxFTrWxtu4GTjP46BDzdTc",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 6,
        "pythBaseDecimal": 8,
    },
    "SRM-USDC": {
        "amm": "7RM8pzbWmGEYJLFuyS5uDyrkd4phcazHppn1C7Qim5nT",
        "poolMint": "DKxkNu5PYoBEWiEZzD9hPsbga145AUZFfRCsieJQbGCP",
        "feeAccount": "7xGiGPPFTiroce8ivKeLgH74WvMbinLqHUTMWwdsSXpp",
        "configAccount": "CuPQhoTH29d5tP9TE2KQMrXqhrMD9ygNhaWDke1fuU7d",
        "pythAccount": "3NBReDRTLKMQEKiLD5tGcx4kXbTf88b7f2xLS9UuGjym",
        "pythPcAccount": "3NBReDRTLKMQEKiLD5tGcx4kXbTf88b7f2xLS9UuGjym",
        "poolCoinTokenAccount": "2qAG2xw2sroQZfRUu5RhvneFm35p9NEtcpJizoFYMn2w",
        "poolCoinMint": "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt",
        "poolPcTokenAccount": "DTmnsxurn7cFSqPMERogJDMKR5NbFjhrJTtFPJbgkW7e",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 6,
        "pythBaseDecimal": 8,
    },
    "GMT-USDC": {
        "amm": "8c511qfb7cYBfQR37hjE4HEB3CuCTo1gDLh9HMtH4Q8D",
        "poolMint": "4nYFycTTt58JKSEnXPFrJ6chLzkGJaoh3rRCjjrADf3N",
        "feeAccount": "EnBuVFNBFzFqET1dXmUpR5vD1bntjXgc11RQANg9ppGA",
        "configAccount": "3tHTVrEApzmRBfEyPbStNLHTXfYbsCneSsSCPFgmgtm5",
        "pythAccount": "DZYZkJcFJThN9nZy4nK3hrHra1LaWeiyoZ9SMdLFEFpY",
        "pythPcAccount": "DZYZkJcFJThN9nZy4nK3hrHra1LaWeiyoZ9SMdLFEFpY",
        "poolCoinTokenAccount": "GPRqn4JjW85dX1qBF3tkdDkPbAzgBC42pYoRFpaxFm8M",
        "poolCoinMint": "7i5KKsX2weiTkry7jA4ZwSuXGhs5eJBEjY8vVxR4pfRx",
        "poolPcTokenAccount": "5jZv8zgxGZtV8zjQUujkeC5bce4WgJVgTYcZKqRQzfKr",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "UXD-USDC": {
        "amm": "5BJUhcBnysAmCpaU6pABof7FUqxx7ZnCZXbctpP48o3C",
        "poolMint": "DM2Grhnear76DwNiRUSfeiFMt6jSj2op9GWinQDc7Yqh",
        "feeAccount": "9pKxj6GTTdJ2biQ6uTyv7CTmVmnjz6cXGCz7rXg7Nm2N",
        "configAccount": "86MM38X9P5mxzRHFVX8ahtB9dCFKSk8AFhb33f5Zz8VW",
        "pythAccount": "3vxLXJqLqF3JG5TCbYycbKWRBbCJQLxQmBGCkyqEEefL",
        "pythPcAccount": "3vxLXJqLqF3JG5TCbYycbKWRBbCJQLxQmBGCkyqEEefL",
        "poolCoinTokenAccount": "5BUkh9e3JF9yUvSw6P3HHqkdMuujRG942hYNSkAEghFs",
        "poolCoinMint": "7kbnvuGBxxj8AG9qp8Scn56muWGaRaFqxg1FsRp3PaFT",
        "poolPcTokenAccount": "BbwCGgAHEUfu7PUEz8hR877aK2snseqorfLbvtcVbjhj",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 6,
        "pythBaseDecimal": 8,
    },
    "LPFi-USDC": {
        "amm": "3AAj2k6URrowQiFHtj7YyRYRxtjAvkwLKaWFjbpwBHJe",
        "poolMint": "2vai6T8NVwHKLCGQC5NDdaGv1Ee26SafUu23gthmTihA",
        "feeAccount": "3q5u5AfAr4NbdYZmhjvtwSv6AFtJ5YBscdrRmkRScQAR",
        "configAccount": "7ECfWXdbaqGT9tTWZenJzkkX92CkZppujWM7NVEq2CxD",
        "pythAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "pythPcAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "poolCoinTokenAccount": "95ELSFcHEvbWoARzTiXLAJfNU76nuZUk3pJCeBANyy99",
        "poolCoinMint": "LPFiNAybMobY5oHfYVdy9jPozFBGKpPiEGoobK2xCe3",
        "poolPcTokenAccount": "FuqMtEqAZipKM2N2as1ucdXfYygG3Pw3jpSytARsjbcD",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 6,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 11,
    },
    "xLPFi-LPFi": {
        "amm": "GYRUyzkU1Jar5Xrrh5ik7aH7PDDBtrL3GSUGKkPrkKSJ",
        "poolMint": "4prhTLCe9TYqSGScpuhnKH3GmsbVbBQN1PbxVomkyHZc",
        "feeAccount": "7NMUEs2GvXiTEfejCRDbF3JLR6FideQBhtoZEa2W9YU7",
        "configAccount": "68bdDQvPGRgSMUqpM3nwJfyrcAYD9UfX2rAdUTusqKu1",
        "pythAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "pythPcAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "poolCoinTokenAccount": "WQ3Cy8z6rVFdptQr6jbQC2wR5qkeX6P7Qm1keWxCuMA",
        "poolCoinMint": "xLPFiPmWve5rUnAYcHZSZWjwgyqEdcV6dDzoBJRtNw9",
        "poolPcTokenAccount": "2nsWtviJca2qmdacJE5P4unu4AMeGPxWmsvjpswGptGg",
        "poolPcMint": "LPFiNAybMobY5oHfYVdy9jPozFBGKpPiEGoobK2xCe3",
        "poolCoinDecimal": 9,
        "poolPcDecimal": 9,
        "poolMintDecimal": 9,
        "pythBaseDecimal": 8,
    },
    "LFNTY-USDC": {
        "amm": "5m1fnYcDdF1TMRVEBdGuSPXt5Sw8ueb9LTopuNL8SJYc",
        "poolMint": "AGytAQTdMJ1jYyDFwgqRUJfzuVUfFm4Kjh4ZnraPbTRv",
        "feeAccount": "7Pa7ssUY264ircqLGXARFvVzENLxGwuXL7ptGJkNinzo",
        "configAccount": "BhKTRa1uhYuSAMsY2SwAGuj5BnxpLPaPpJwArKxZvjYK",
        "pythAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "pythPcAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "poolCoinTokenAccount": "3T9zHCguVtKfgzaUvdBne4V8LReeiAMAzmRbWwt69gwJ",
        "poolCoinMint": "LFNTYraetVioAPnGJht4yNg2aUZFXR776cMeN9VMjXp",
        "poolPcTokenAccount": "F3fuSs91bGysoZFgNDbGrPonEtCBaGRDMpHGMwfgxzsP",
        "poolPcMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 6,
        "pythBaseDecimal": 8,
    },
    "xLFNTY-LFNTY": {
        "amm": "8XyjVmw2FCajAcQ8f5vJH2i6qtBLqG6nzESoQrP5yFvS",
        "poolMint": "F5v7Akz18dM3KpkicJiwCjqQRyX5f7RgU1Aarf92HCYz",
        "feeAccount": "8T2wLBxppM1YiPhMpREMUUDcNbWrfrrAY5wEgPcskoqa",
        "configAccount": "7ZNNPhxRZPRrrvLBfutiLQt9LwDGfwCkvNfmbeuGkDev",
        "pythAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "pythPcAccount": "GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
        "poolCoinTokenAccount": "987aQuFhpV9HAQBnsq4xuLxL2jVBCDSV3wXtgrJrwMc6",
        "poolCoinMint": "xLfNTYy76B8Tiix3hA51Jyvc1kMSFV4sPdR7szTZsRu",
        "poolPcTokenAccount": "8M4mgMPDZ9exEahfhGYdWnJ2GEMRdk8b6EaxsMg1XVyg",
        "poolPcMint": "LFNTYraetVioAPnGJht4yNg2aUZFXR776cMeN9VMjXp",
        "poolCoinDecimal": 6,
        "poolPcDecimal": 6,
        "poolMintDecimal": 6,
        "pythBaseDecimal": 8,
    }
}

instructions_v1 = {
    "version": "0.1.0",
    "name": "lifinity_amm",
    "instructions": [
        {"name": "initialize",
            "accounts": [
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "feeAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "pythAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "pythPcAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "baseDecimals",
                    "type": "u8",
                },
                {
                    "name": "feesInput",
                    "type": {
                        "defined": "FeesInput",
                    },
                },
                {
                    "name": "curveInput",
                    "type": {
                        "defined": "CurveInput",
                    },
                },
                {
                    "name": "configInput",
                    "type": {
                        "defined": "ConfigInput",
                    },
                }
            ],
         },
        {
            "name": "swap",
            "accounts": [
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthority",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destinationInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "swapSource",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "swapDestination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "feeAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "pythAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "pythPcAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "amountIn",
                    "type": "u64",
                },
                {
                    "name": "minimumAmountOut",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "depositAllTokenTypes",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthorityInfo",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceAInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "sourceBInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "poolTokenAmount",
                    "type": "u64",
                },
                {
                    "name": "maximumTokenAAmount",
                    "type": "u64",
                },
                {
                    "name": "maximumTokenBAmount",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "withdrawAllTokenTypes",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthorityInfo",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destTokenAInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destTokenBInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "feeAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "poolTokenAmount",
                    "type": "u64",
                },
                {
                    "name": "minimumTokenAAmount",
                    "type": "u64",
                },
                {
                    "name": "minimumTokenBAmount",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "configUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "configInput",
                    "type": {
                        "defined": "ConfigInput",
                    },
                }
            ],
        },
        {
            "name": "oracleStatusUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "oracleStatus",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "ammUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "freezeTrade",
                    "type": "u8",
                },
                {
                    "name": "freezeDeposit",
                    "type": "u8",
                },
                {
                    "name": "freezeWithdraw",
                    "type": "u8",
                },
                {
                    "name": "baseDecimals",
                    "type": "u8",
                }
            ],
        },
        {
            "name": "ammCapTargetUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "cap",
                    "type": "u64",
                },
                {
                    "name": "target",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "ammFeeCurveUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "feesInput",
                    "type": {
                        "defined": "FeesInput",
                    },
                },
                {
                    "name": "curveInput",
                    "type": {
                        "defined": "CurveInput",
                    },
                }
            ],
        },
        {
            "name": "ammPythUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "pythAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "pythPcAccount",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [],
        },
        {
            "name": "priceUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "lastPrice",
                    "type": "u64",
                },
                {
                    "name": "lastBalancedPrice",
                    "type": "u64",
                },
                {
                    "name": "concentrationRatio",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "oracleStatusUpdateUi",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "oracleStatus",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "freezeUpdateUi",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "freezeTrade",
                    "type": "u8",
                },
                {
                    "name": "freezeDeposit",
                    "type": "u8",
                },
                {
                    "name": "freezeWithdraw",
                    "type": "u8",
                }
            ],
        },
        {
            "name": "feesUpdateUi",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "feesInput",
                    "type": {
                        "defined": "FeesInput",
                    },
                }
            ],
        },
        {
            "name": "targetUpdateUi",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "cap",
                    "type": "u64",
                },
                {
                    "name": "target",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "configFeeUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "configAccount",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "feeAccount",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [],
        },
        {
            "name": "ammFeeUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "tradeFee",
                    "type": "u64",
                },
                {
                    "name": "ownerFee",
                    "type": "u64",
                }
            ],
        }
    ],
    "accounts": [
        {
            "name": "amm",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "initializerKey",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerDepositTokenAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerReceiveTokenAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerAmount",
                        "type": "u64",
                    },
                    {
                        "name": "takerAmount",
                        "type": "u64",
                    },
                    {
                        "name": "isInitialized",
                        "type": "bool",
                    },
                    {
                        "name": "bumpSeed",
                        "type": "u8",
                    },
                    {
                        "name": "freezeTrade",
                        "type": "u8",
                    },
                    {
                        "name": "freezeDeposit",
                        "type": "u8",
                    },
                    {
                        "name": "freezeWithdraw",
                        "type": "u8",
                    },
                    {
                        "name": "baseDecimals",
                        "type": "u8",
                    },
                    {
                        "name": "tokenProgramId",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenAAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenBAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "poolMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenAMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenBMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "poolFeeAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "pythAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "pythPcAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "configAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammTemp1",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammTemp2",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammTemp3",
                        "type": "publicKey",
                    },
                    {
                        "name": "fees",
                        "type": {
                            "defined": "FeesInput",
                        },
                    },
                    {
                        "name": "curve",
                        "type": {
                            "defined": "CurveInput",
                        },
                    }
                ],
            },
        },
        {
            "name": "config",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "concentrationRatio",
                        "type": "u64",
                    },
                    {
                        "name": "lastPrice",
                        "type": "u64",
                    },
                    {
                        "name": "adjustRatio",
                        "type": "u64",
                    },
                    {
                        "name": "balanceRatio",
                        "type": "u64",
                    },
                    {
                        "name": "lastBalancedPrice",
                        "type": "u64",
                    },
                    {
                        "name": "configDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "pythConfidenceLimit",
                        "type": "u64",
                    },
                    {
                        "name": "pythSlotLimit",
                        "type": "u64",
                    },
                    {
                        "name": "volumeX",
                        "type": "u64",
                    },
                    {
                        "name": "volumeY",
                        "type": "u64",
                    },
                    {
                        "name": "volumeXInY",
                        "type": "u64",
                    },
                    {
                        "name": "coefficientUp",
                        "type": "u64",
                    },
                    {
                        "name": "coefficientDown",
                        "type": "u64",
                    },
                    {
                        "name": "oracleStatus",
                        "type": "u64",
                    },
                    {
                        "name": "tradeFeeLp",
                        "type": "u64",
                    },
                    {
                        "name": "platformFeeLp",
                        "type": "u64",
                    }
                ],
            },
        }
    ],
    "types": [
        {
            "name": "CurveFees",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "tradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "tradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeDenominator",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "FeesInput",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "tradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "tradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeDenominator",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "CurveInput",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "curveType",
                        "type": "u8",
                    },
                    {
                        "name": "curveParameters",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "ConfigInput",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "concentrationRatio",
                        "type": "u64",
                    },
                    {
                        "name": "lastPrice",
                        "type": "u64",
                    },
                    {
                        "name": "adjustRatio",
                        "type": "u64",
                    },
                    {
                        "name": "balanceRatio",
                        "type": "u64",
                    },
                    {
                        "name": "lastBalancedPrice",
                        "type": "u64",
                    },
                    {
                        "name": "configDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "pythConfidenceLimit",
                        "type": "u64",
                    },
                    {
                        "name": "pythSlotLimit",
                        "type": "u64",
                    },
                    {
                        "name": "volumeX",
                        "type": "u64",
                    },
                    {
                        "name": "volumeY",
                        "type": "u64",
                    },
                    {
                        "name": "volumeXInY",
                        "type": "u64",
                    },
                    {
                        "name": "coefficientUp",
                        "type": "u64",
                    },
                    {
                        "name": "coefficientDown",
                        "type": "u64",
                    },
                    {
                        "name": "oracleStatus",
                        "type": "u64",
                    },
                    {
                        "name": "tradeFeeLp",
                        "type": "u64",
                    },
                    {
                        "name": "platformFeeLp",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "CurveType",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "ConstantProduct",
                    },
                    {
                        "name": "Stable",
                    }
                ],
            },
        },
        {
            "name": "TradeDirection",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "AtoB",
                    },
                    {
                        "name": "BtoA",
                    }
                ],
            },
        },
        {
            "name": "RoundDirection",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "Floor",
                    },
                    {
                        "name": "Ceiling",
                    }
                ],
            },
        }
    ],
    "errors": [
        {
            "code": 6000,
            "name": "AlreadyInUse",
            "msg": "Swap account already in use",
        },
        {
            "code": 6001,
            "name": "InvalidProgramAddress",
            "msg": "Invalid program address generated from bump seed and key",
        },
        {
            "code": 6002,
            "name": "InvalidOwner",
            "msg": "Input account owner is not the program address",
        },
        {
            "code": 6003,
            "name": "InvalidOutputOwner",
            "msg": "Output pool account owner cannot be the program address",
        },
        {
            "code": 6004,
            "name": "ExpectedMint",
            "msg": "Deserialized account is not an SPL Token mint",
        },
        {
            "code": 6005,
            "name": "ExpectedAccount",
            "msg": "Deserialized account is not an SPL Token account",
        },
        {
            "code": 6006,
            "name": "EmptySupply",
            "msg": "Input token account empty",
        },
        {
            "code": 6007,
            "name": "InvalidSupply",
            "msg": "Pool token mint has a non-zero supply",
        },
        {
            "code": 6008,
            "name": "InvalidDelegate",
            "msg": "Token account has a delegate",
        },
        {
            "code": 6009,
            "name": "InvalidInput",
            "msg": "InvalidInput",
        },
        {
            "code": 6010,
            "name": "IncorrectSwapAccount",
            "msg": "Address of the provided swap token account is incorrect",
        },
        {
            "code": 6011,
            "name": "IncorrectPoolMint",
            "msg": "Address of the provided pool token mint is incorrect",
        },
        {
            "code": 6012,
            "name": "InvalidOutput",
            "msg": "InvalidOutput",
        },
        {
            "code": 6013,
            "name": "CalculationFailure",
            "msg": "General calculation failure due to overflow or underflow",
        },
        {
            "code": 6014,
            "name": "InvalidInstruction",
            "msg": "Invalid instruction",
        },
        {
            "code": 6015,
            "name": "RepeatedMint",
            "msg": "Swap input token accounts have the same mint",
        },
        {
            "code": 6016,
            "name": "ExceededSlippage",
            "msg": "Swap instruction exceeds desired slippage limit",
        },
        {
            "code": 6017,
            "name": "InvalidCloseAuthority",
            "msg": "Token account has a close authority",
        },
        {
            "code": 6018,
            "name": "InvalidFreezeAuthority",
            "msg": "Pool token mint has a freeze authority",
        },
        {
            "code": 6019,
            "name": "IncorrectFeeAccount",
            "msg": "Pool fee token account incorrect",
        },
        {
            "code": 6020,
            "name": "ZeroTradingTokens",
            "msg": "Given pool token amount results in zero trading tokens",
        },
        {
            "code": 6021,
            "name": "FeeCalculationFailure",
            "msg": "Fee calculation failed due to overflow, underflow, or unexpected 0",
        },
        {
            "code": 6022,
            "name": "ConversionFailure",
            "msg": "Conversion to u64 failed with an overflow or underflow",
        },
        {
            "code": 6023,
            "name": "InvalidFee",
            "msg": "The provided fee does not match the program owner's constraints",
        },
        {
            "code": 6024,
            "name": "IncorrectTokenProgramId",
            "msg": "The provided token program does not match the token program expected by the swap",
        },
        {
            "code": 6025,
            "name": "IncorrectOracleAccount",
            "msg": "Address of the provided oracle account is incorrect",
        },
        {
            "code": 6026,
            "name": "IncorrectConfigAccount",
            "msg": "Address of the provided config account is incorrect",
        },
        {
            "code": 6027,
            "name": "UnsupportedCurveType",
            "msg": "The provided curve type is not supported by the program owner",
        },
        {
            "code": 6028,
            "name": "InvalidCurve",
            "msg": "The provided curve parameters are invalid",
        },
        {
            "code": 6029,
            "name": "UnsupportedCurveOperation",
            "msg": "The operation cannot be performed on the given curve",
        },
        {
            "code": 6030,
            "name": "InvalidPythStatus",
            "msg": "Pyth oracle status is not 'trading'",
        },
        {
            "code": 6031,
            "name": "InvalidPythPrice",
            "msg": "Could not retrieve updated price feed from the Pyth oracle",
        },
        {
            "code": 6032,
            "name": "IncorrectSigner",
            "msg": "Address of the provided signer account is incorrect",
        },
        {
            "code": 6033,
            "name": "ExceedPoolBalance",
            "msg": "Swap amount exceeds pool balance",
        },
        {
            "code": 6034,
            "name": "ProgramIsFrozen",
            "msg": "Program is frozen",
        },
        {
            "code": 6035,
            "name": "OracleConfidence",
            "msg": "Oracle confidence is too low",
        },
        {
            "code": 6036,
            "name": "OverCapAmount",
            "msg": "Over Pool Cap Amount",
        },
        {
            "code": 6037,
            "name": "InvalidUpdateAccount",
            "msg": "Invalid update wallet address",
        }
    ]
}


instructions_v2 = {
    "version": "0.1.1",
    "name": "lifinity_amm_v2",
    "instructions": [
        {
            "name": "initialize",
            "accounts": [
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "feeAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "oracleMainAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "oracleSubAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "oraclePcAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "baseDecimals",
                    "type": "u8",
                },
                {
                    "name": "ammFees",
                    "type": {
                        "defined": "AmmFees",
                    },
                },
                {
                    "name": "ammCurve",
                    "type": {
                        "defined": "AmmCurve",
                    },
                },
                {
                    "name": "ammConfig",
                    "type": {
                        "defined": "AmmConfig",
                    },
                }
            ],
        },
        {
            "name": "swap",
            "accounts": [
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthority",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destinationInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "swapSource",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "swapDestination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "feeAccount",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "oracleMainAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "oracleSubAccount",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "oraclePcAccount",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "amountIn",
                    "type": "u64",
                },
                {
                    "name": "minimumAmountOut",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "depositAllTokenTypes",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthorityInfo",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceAInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "sourceBInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destination",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "poolTokenAmount",
                    "type": "u64",
                },
                {
                    "name": "maximumTokenAAmount",
                    "type": "u64",
                },
                {
                    "name": "maximumTokenBAmount",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "withdrawAllTokenTypes",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "authority",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "userTransferAuthorityInfo",
                    "isMut": False,
                    "isSigner": True,
                },
                {
                    "name": "sourceInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenA",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenB",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "poolMint",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destTokenAInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "destTokenBInfo",
                    "isMut": True,
                    "isSigner": False,
                },
                {
                    "name": "tokenProgram",
                    "isMut": False,
                    "isSigner": False,
                }
            ],
            "args": [
                {
                    "name": "poolTokenAmount",
                    "type": "u64",
                },
                {
                    "name": "minimumTokenAAmount",
                    "type": "u64",
                },
                {
                    "name": "minimumTokenBAmount",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "ammOracleStatusUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "oracleStatus",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "ammFreezeUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "freezeTrade",
                    "type": "u8",
                },
                {
                    "name": "freezeDeposit",
                    "type": "u8",
                },
                {
                    "name": "freezeWithdraw",
                    "type": "u8",
                },
                {
                    "name": "baseDecimals",
                    "type": "u8",
                }
            ],
        },
        {
            "name": "ammFeeCurveConfigUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "ammFees",
                    "type": {
                        "defined": "AmmFees",
                    },
                },
                {
                    "name": "ammCurve",
                    "type": {
                        "defined": "AmmCurve",
                    },
                },
                {
                    "name": "ammConfig",
                    "type": {
                        "defined": "AmmConfig",
                    },
                }
            ],
        },
        {
            "name": "ammLastPriceUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": True,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "lastPrice",
                    "type": "u64",
                }
            ],
        },
        {
            "name": "ammRegressionTargetUpdate",
            "accounts": [
                {
                    "name": "amm",
                    "isMut": False,
                    "isSigner": False,
                },
                {
                    "name": "ammOwner",
                    "isMut": False,
                    "isSigner": True,
                }
            ],
            "args": [
                {
                    "name": "targetAmount",
                    "type": "u64",
                }
            ],
        }
    ],
    "accounts": [
        {
            "name": "amm",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "initializerKey",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerDepositTokenAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerReceiveTokenAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "initializerAmount",
                        "type": "u64",
                    },
                    {
                        "name": "takerAmount",
                        "type": "u64",
                    },
                    {
                        "name": "isInitialized",
                        "type": "bool",
                    },
                    {
                        "name": "bumpSeed",
                        "type": "u8",
                    },
                    {
                        "name": "freezeTrade",
                        "type": "u8",
                    },
                    {
                        "name": "freezeDeposit",
                        "type": "u8",
                    },
                    {
                        "name": "freezeWithdraw",
                        "type": "u8",
                    },
                    {
                        "name": "baseDecimals",
                        "type": "u8",
                    },
                    {
                        "name": "tokenProgramId",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenAAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenBAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "poolMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenAMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "tokenBMint",
                        "type": "publicKey",
                    },
                    {
                        "name": "feeAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "oracleMainAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "oracleSubAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "oraclePcAccount",
                        "type": "publicKey",
                    },
                    {
                        "name": "fees",
                        "type": {
                            "defined": "AmmFees",
                        },
                    },
                    {
                        "name": "curve",
                        "type": {
                            "defined": "AmmCurve",
                        },
                    },
                    {
                        "name": "config",
                        "type": {
                            "defined": "AmmConfig",
                        },
                    },
                    {
                        "name": "ammPTemp1",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammPTemp2",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammPTemp3",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammPTemp4",
                        "type": "publicKey",
                    },
                    {
                        "name": "ammPTemp5",
                        "type": "publicKey",
                    }
                ],
            },
        }
    ],
    "types": [
        {
            "name": "AmmFees",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "tradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "tradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerTradeFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "ownerWithdrawFeeDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeNumerator",
                        "type": "u64",
                    },
                    {
                        "name": "hostFeeDenominator",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "AmmCurve",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "curveType",
                        "type": "u8",
                    },
                    {
                        "name": "curveParameters",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "AmmConfig",
            "type": {
                "kind": "struct",
                "fields": [
                    {
                        "name": "lastPrice",
                        "type": "u64",
                    },
                    {
                        "name": "lastBalancedPrice",
                        "type": "u64",
                    },
                    {
                        "name": "configDenominator",
                        "type": "u64",
                    },
                    {
                        "name": "volumeX",
                        "type": "u64",
                    },
                    {
                        "name": "volumeY",
                        "type": "u64",
                    },
                    {
                        "name": "volumeXInY",
                        "type": "u64",
                    },
                    {
                        "name": "depositCap",
                        "type": "u64",
                    },
                    {
                        "name": "regressionTarget",
                        "type": "u64",
                    },
                    {
                        "name": "oracleType",
                        "type": "u64",
                    },
                    {
                        "name": "oracleStatus",
                        "type": "u64",
                    },
                    {
                        "name": "oracleMainSlotLimit",
                        "type": "u64",
                    },
                    {
                        "name": "oracleSubConfidenceLimit",
                        "type": "u64",
                    },
                    {
                        "name": "oracleSubSlotLimit",
                        "type": "u64",
                    },
                    {
                        "name": "oraclePcConfidenceLimit",
                        "type": "u64",
                    },
                    {
                        "name": "oraclePcSlotLimit",
                        "type": "u64",
                    },
                    {
                        "name": "stdSpread",
                        "type": "u64",
                    },
                    {
                        "name": "stdSpreadBuffer",
                        "type": "u64",
                    },
                    {
                        "name": "spreadCoefficient",
                        "type": "u64",
                    },
                    {
                        "name": "priceBufferCoin",
                        "type": "i64",
                    },
                    {
                        "name": "priceBufferPc",
                        "type": "i64",
                    },
                    {
                        "name": "rebalanceRatio",
                        "type": "u64",
                    },
                    {
                        "name": "feeTrade",
                        "type": "u64",
                    },
                    {
                        "name": "feePlatform",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp3",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp4",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp5",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp6",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp7",
                        "type": "u64",
                    },
                    {
                        "name": "configTemp8",
                        "type": "u64",
                    }
                ],
            },
        },
        {
            "name": "CurveType",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "Standard",
                    },
                    {
                        "name": "ConstantProduct",
                    }
                ],
            },
        },
        {
            "name": "TradeDirection",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "AtoB",
                    },
                    {
                        "name": "BtoA",
                    }
                ],
            },
        },
        {
            "name": "RoundDirection",
            "type": {
                "kind": "enum",
                "variants": [
                    {
                        "name": "Floor",
                    },
                    {
                        "name": "Ceiling",
                    }
                ],
            },
        }
    ],
    "errors": [
        {
            "code": 6000,
            "name": "AlreadyInUse",
            "msg": "Swap account already in use",
        },
        {
            "code": 6001,
            "name": "InvalidProgramAddress",
            "msg": "Invalid program address generated from bump seed and key",
        },
        {
            "code": 6002,
            "name": "InvalidOwner",
            "msg": "Input account owner is not the program address",
        },
        {
            "code": 6003,
            "name": "InvalidOutputOwner",
            "msg": "Output pool account owner cannot be the program address",
        },
        {
            "code": 6004,
            "name": "ExpectedMint",
            "msg": "Deserialized account is not an SPL Token mint",
        },
        {
            "code": 6005,
            "name": "ExpectedAccount",
            "msg": "Deserialized account is not an SPL Token account",
        },
        {
            "code": 6006,
            "name": "EmptySupply",
            "msg": "Input token account empty",
        },
        {
            "code": 6007,
            "name": "InvalidSupply",
            "msg": "Pool token mint has a non-zero supply",
        },
        {
            "code": 6008,
            "name": "InvalidDelegate",
            "msg": "Token account has a delegate",
        },
        {
            "code": 6009,
            "name": "InvalidInput",
            "msg": "InvalidInput",
        },
        {
            "code": 6010,
            "name": "IncorrectSwapAccount",
            "msg": "Address of the provided swap token account is incorrect",
        },
        {
            "code": 6011,
            "name": "IncorrectPoolMint",
            "msg": "Address of the provided pool token mint is incorrect",
        },
        {
            "code": 6012,
            "name": "InvalidOutput",
            "msg": "InvalidOutput",
        },
        {
            "code": 6013,
            "name": "CalculationFailure",
            "msg": "General calculation failure due to overflow or underflow",
        },
        {
            "code": 6014,
            "name": "InvalidInstruction",
            "msg": "Invalid instruction",
        },
        {
            "code": 6015,
            "name": "RepeatedMint",
            "msg": "Swap input token accounts have the same mint",
        },
        {
            "code": 6016,
            "name": "ExceededSlippage",
            "msg": "Swap instruction exceeds desired slippage limit",
        },
        {
            "code": 6017,
            "name": "InvalidCloseAuthority",
            "msg": "Token account has a close authority",
        },
        {
            "code": 6018,
            "name": "InvalidFreezeAuthority",
            "msg": "Pool token mint has a freeze authority",
        },
        {
            "code": 6019,
            "name": "IncorrectFeeAccount",
            "msg": "Pool fee token account incorrect",
        },
        {
            "code": 6020,
            "name": "ZeroTradingTokens",
            "msg": "Given pool token amount results in zero trading tokens",
        },
        {
            "code": 6021,
            "name": "FeeCalculationFailure",
            "msg": "Fee calculation failed due to overflow, underflow, or unexpected 0",
        },
        {
            "code": 6022,
            "name": "ConversionFailure",
            "msg": "Conversion to u64 failed with an overflow or underflow",
        },
        {
            "code": 6023,
            "name": "InvalidFee",
            "msg": "The provided fee does not match the program owner's constraints",
        },
        {
            "code": 6024,
            "name": "IncorrectTokenProgramId",
            "msg": "The provided token program does not match the token program expected by the swap",
        },
        {
            "code": 6025,
            "name": "IncorrectOracleAccount",
            "msg": "Address of the provided oracle account is incorrect",
        },
        {
            "code": 6026,
            "name": "IncorrectConfigAccount",
            "msg": "Address of the provided config account is incorrect",
        },
        {
            "code": 6027,
            "name": "UnsupportedCurveType",
            "msg": "The provided curve type is not supported by the program owner",
        },
        {
            "code": 6028,
            "name": "InvalidCurve",
            "msg": "The provided curve parameters are invalid",
        },
        {
            "code": 6029,
            "name": "UnsupportedCurveOperation",
            "msg": "The operation cannot be performed on the given curve",
        },
        {
            "code": 6030,
            "name": "InvalidPythStatus",
            "msg": "Pyth oracle status is not 'trading'",
        },
        {
            "code": 6031,
            "name": "InvalidPythPrice",
            "msg": "Could not retrieve updated price feed from the Pyth oracle",
        },
        {
            "code": 6032,
            "name": "IncorrectSigner",
            "msg": "Address of the provided signer account is incorrect",
        },
        {
            "code": 6033,
            "name": "ExceedPoolBalance",
            "msg": "Swap amount exceeds pool balance",
        },
        {
            "code": 6034,
            "name": "ProgramIsFrozen",
            "msg": "Program is frozen",
        },
        {
            "code": 6035,
            "name": "OracleConfidence",
            "msg": "Oracle confidence is too low",
        },
        {
            "code": 6036,
            "name": "OverCapAmount",
            "msg": "Over Pool Cap Amount",
        },
        {
            "code": 6037,
            "name": "InvalidUpdateAccount",
            "msg": "Invalid update wallet address",
        }
    ]
}
