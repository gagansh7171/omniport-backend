import swapper
from django.db import models
from django_countries import fields as django_countries_fields

from kernel.models.personal_information.base import AbstractPersonalInformation


class AbstractPoliticalInformation(AbstractPersonalInformation):
    """
    This model holds political information about a person
    """

    nationality = django_countries_fields.CountryField(
        blank_label='Nationality',
    )

    religion = models.CharField(
        max_length=63,
        blank=True,
    )

    passport_number = models.CharField(
        max_length=15,
        blank=True,
    )
    driving_license_number = models.CharField(
        max_length=31,
        blank=True,
    )

    class Meta:
        """
        Meta class for AbstractPoliticalInformation
        """

        abstract = True

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        person = self.person
        nationality = self.nationality
        return f'{person} - {nationality}'


class PoliticalInformation(AbstractPoliticalInformation):
    """
    This class implements AbstractPoliticalInformation
    """

    class Meta:
        """
        Meta class for PoliticalInformation
        """

        verbose_name_plural = 'political information'
        swappable = swapper.swappable_setting('kernel',
                                              'PoliticalInformation')
