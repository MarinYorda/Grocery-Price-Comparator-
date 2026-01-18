import argparse
from dataclasses import dataclass
from typing import List, Optional

SUPPORTED_PROVIDERS = ["provigo", "maxi", "metro", "iga"]

@dataclass
class CLIArgs:
    postal_code: str
    radius_km: float
    providers: List[str]
    limit: int
    output: str
    csv_path: str 


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="grocery-price-comparator",
        description=(
            "\n -------------------------------------\n"
            "\n" 
            "Compare grocery prices across nearby stores using store APIs.\n "
            "\n"
            "Use --help to see all available options"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--postal-code",
        metavar=" CODE",
        help="Postal code used to find nearby stores (ex. 'H5E 1Y4'). If ommited runs Stage 1 demo mode.",
    )

    parser.add_argument(
        "--radius-km",
        type=float,
        default=5.0,
        metavar="KM",
        help="Search radius in kilometers (default: 5m)",
    )

    parser.add_argument(
        "--provider",
        nargs="+",
        metavar="STORE",
        choices=SUPPORTED_PROVIDERS,
        default=["provigo"],
        help="Store providers to query (default: provigo)."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Max number of products to process (default: 50)."
    )
    parser.add_argument(
        "--output",
        choices=["print", "csv", "both"],
        metavar="MODE",
        default="both",
        help="Output mode"
    )
    parser.add_argument(
        "--csv-path",
        metavar="PATH",
        default="comparison_results.csv",
        help="CSV output path (default: comparison_results.csv)."
    )

    parser.add_argument(
        "--demo-json",
        action="store_true",
        help="Run Stage 1 demo using local JSON files (raw data mode).",
    )

    
    return parser

def parse_args():
    parser = build_parser()
    args = parser.parse_args()

    # Normalizing user provided info
    if args.postal_code is not None:
        args.postal_code = str(args.postal_code).strip().upper()

        if args.radius_km <= 0:
            parser.error("-- radiums-km must be greater than 0.")
        if args.limit <= 0:
            parser.error("--limit must be greater than 0.")

    return args