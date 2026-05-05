import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
      # Network Settings
    SOLANA_RPC: str = "https://api.mainnet-beta.solana.com"
    TON_RPC: str = "https://toncenter.com/api/v2/jsonRPC"
    
    # Arbitration Settings
    MIN_PROFIT_PERCENT: float = 1.2
    MAX_SLIPPAGE: float = 0.5
    MEV_PROTECTION: bool = True

    class Config:
        env_file = ".env"

config = Settings()
