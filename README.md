# JimSim 
DeFi Yield Analysis Platform.
This repo contains the code for the data backend.

## Demo Video
https://youtu.be/_qmZON9IM00

## Summary
JimSim is aimed at retail and institutional investors, tired of analysing and validating yield metrics displayed differently by every single yield protocol. A standard has to be established to provide transparency and to build trust in the industry. Trust that is utterly necessary after the painful events with Luna and FTX.

And we don't have to look far to find metrics which can assess returns and risks of yield-bearing investment products - and if we are honest to each other, that's what DeFi yield protocols offer: investment products that provide a return. In TradFi there are tons of metrics being used to assess the return and risk of investment products. Profit, Loss, Profit Factor, Drawdown, Volatility, and even metrics like Sharpe Ratio, Sortino Ratio and Treynor Ratio.

But none of the DeFi data platforms provide these metrics.

For the scope of this hackathon we aimed at collecting the data and getting it into a consumable format so that we can do the necessary calculations for these metrics in the next step.

## Challenges

"DeFi is transparent and the solution to all our CeFi problems" - not quite! Data is freely available but without expert knowledge hard to understand, interpret and collect. Four our specific use case the majority of time went into understanding the different yield products, which operations for instance a liquidity pool performs and from which data points we can derive profit, loss, volatility and other metrics.

Another chunk of time went into analysing which data we can already collect from different APIs that are available in the market. We looked at Helius, Solscan, Hellomoon and the protocols native APIs and analysed whether the required data point were provided. One of the conclusion we arrived at was that historical data is extremely, if not even mere impossible to get. Unless you spend thousands of dollars to get access to historic blocklevel on-chaind data and analyse billions of transactions and the indluded instructions (out of scope for this hackathon).

At the end we were happy to have been able to collect the necessary data points from Orca's API, whose team has been very helpful. Hellomoon has also been very helpful, up to the point where they spend an allnighter just to fix some things on their end and provide us the data. Big kudos to both teams. Always great to see the quality of teams in the Solana ecosystem <3 !!!

## Design 
 The design for the DeFi yield analysis system consists of the following 
 * Pool Master Data Collectors - collects off chain information regarding liquidity pools from various AMM protocols 
 * Pool Transactions Collectors - Collect activities likes Deposits, Withdrawls, Emisssions, Swaps, Fees from the Chain 
 * Data Aggregator Service - Standardize, Aggregate and summarize transactional data. Calculate and publish key metrics like Risk rate, Loss rate, APRs etc.
 * Data Visualization - Visualize the data view via a browser based UI (not part of the hackathon scope)

## Data Points considered for the Prototype
- Pool Balance in USD
- Withdrawals - remove liquidity
- Deposits -add liquidity
- Trades/Swaps
- LP Fees
- Swap Fees
- Amount of Liquidity Providers
- Pool ID
- Pool Account
- Token A Amount
- Token B Amount
- Pool Balance in Token
- Token Prices in USD

## Data Sources
- Hellomoon
- Solscan
- Coingecko
- Orca API
