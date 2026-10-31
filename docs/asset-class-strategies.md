# Asset-class strategies (v0.56)

Research playbooks only. Scores on synthetic data.

## Major (BTC/ETH style)
Adaptive multi-factor: EMA cross, Supertrend, Ichimoku cloud, Bollinger, Keltner, VWAP, MACD, Heikin-Ashi, Parabolic SAR, Donchian, GARCH/EWMA vol forecast, funding/on-chain/OI/order-flow/liquidity proxies. Correlation-adjusted outside stress. Risk cap 8%.

## Large-cap alt
Volume-profile breakout + VWAP + MACD + multi-TF + relative strength z-score + regime cluster + volume delta + netflow + OI + order-flow. Cap 4%.

## Stablecoin
Adaptive peg deviation with volume + netflow + liquidity depth confirmation. Cap 0%.

## DeFi
Calm multi-scale + low anomaly + Supertrend + ADX + on-chain activity/smart-money + isolation + risk-parity + CVaR. Cap 2%.

## Meme
Qualified burst + StochRSI + hard horizon + volume-flow decay + anomaly/residual/liq heat/order-flow filter. Cap 0.5%.

## L2
Relative strength + MACD vs benchmark + adaptive MTF + correlation + cluster + vol forecast + transition probability. Cap 3%.

## RWA
Slow multi-scale + gap/anomaly halt + volume + isolation + forecast + CVaR. Cap 2%.

## Perpetual
Negative funding carry + contained drift + low anomaly + funding flip + correlation + residual + OI + order-flow. Cap 2%.

## AI-token
Hybrid burst + activity proxy + divergence + low isolation + strict horizon + smart-money + OI + transition. Cap 1%.

All include multi-horizon consistency, RSI/MACD/Stoch divergence, regime clustering (k-means + HMM + transition), adaptive Kelly/risk-parity/CVaR sizing research.
