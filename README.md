# jimsim-app
A repo for Solana DeFi Dashboard 

## Summary

## Overview

## Design 
 The design for the DeFi Dashboard system consists of the following 
 * Pool Master Data Collectors - collects off chain information regarding pool from various DeFi protocol projects 
 * Pool transactions collectors - Collect activities likes Deposits, Withdrawls, Emisssions, Swaps, Fees from the Chain 
 * Data Aggregator service - Standardize, Aggregate and summarize transactional data. Calculate and publish key metrics like Risk rate, Loss rate, APRs etc.
 * Data Visualization - Visualize the data view via a browser based UI

## Data points considered for the mvp.
- pool balance in USD
- withdrawals/remove liquidity
- deposits/add liquidity
- trades/swaps
- fees
- current amount of stakers/LPs (maybe)
- poolId
- poolAccount
- tokenAAmount
- tokenBAmount
- poolTokenSupply
