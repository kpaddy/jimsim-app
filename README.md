# JimSim 
DeFi Yield Analysis Platform. <b>

## Summary

## Overview

## Design 
 The design for the DeFi Dashboard system consists of the following 
 * Pool Master Data Collectors - collects off chain information regarding liquidity pools from various AMM protocols 
 * Pool transactions collectors - Collect activities likes Deposits, Withdrawls, Emisssions, Swaps, Fees from the Chain 
 * Data Aggregator service - Standardize, Aggregate and summarize transactional data. Calculate and publish key metrics like Risk rate, Loss rate, APRs etc.
 * Data Visualization - Visualize the data view via a browser based UI

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
