import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)


class Cafe:
    def __init__(self, name: str) -> None:
        """Initialize the cafe with a name."""
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Checks if a visitor is allowed to enter the cafe."""

        # Check if the visitor has been vaccinated
        if "vaccine" not in visitor:
            raise NotVaccinatedError(
                f"{visitor["name"]} is not vaccinated."
            )

        # Check if the vaccine is expired
        expiration_date = visitor["vaccine"].get("expiration_date")
        if expiration_date < datetime.date.today():
            raise OutdatedVaccineError(
                f"{visitor["name"]}'s vaccine is outdated."
            )

        # Check if the visitor is wearing a mask
        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError(
                f"{visitor["name"]} is not wearing a mask."
            )

        return f"Welcome to {self.name}"
