import datetime
import nose

from django.utils import unittest
from django.core.exceptions import ValidationError

from dorsia.models import Reservation
from . import model_helpers

class ReservationTestCase( unittest.TestCase ):
    """
    Tests reservation model
    """

    def setUp( self ):
        self.reservation = Reservation( name = "Patrick Bateman",
                                        email = "patrick.bateman@pierce.com",
                                        partySize = 5,
                                        reservationDate = datetime.date.today(),
                                        seatingTime = 8 )


    def tearDown( self ):
        pass
        # self.reservation.delete()


    def testHasNameField( self ):
        self.assertTrue( model_helpers.modelHasField( Reservation, "name" ) )


    def testHasEmailField( self ):
        self.assertTrue( model_helpers.modelHasField( Reservation, "email" ) )


    def testHasPartySizeField( self ):
        self.assertTrue( model_helpers.modelHasField( Reservation, "partySize" ) )


    def testHasReservationDateField( self ):
        self.assertTrue( model_helpers.modelHasField( Reservation, "reservationDate" ) )


    def testHasSeatingTimeField( self ):
        self.assertTrue( model_helpers.modelHasField( Reservation, "seatingTime" ) )


    def testValidFields( self ):
        self.assertEqual( self.reservation.clean_fields(), None )


    def testNoName( self ):
        self.reservation.name = None
        with self.assertRaises( ValidationError ):
            self.reservation.clean_fields()


    def testLongName( self ):
        self.reservation.name = "a" * 101
        with self.assertRaises( ValidationError ):
            self.reservation.clean_fields()


    def testNoEmail( self ):
        self.reservation.email = None
        with self.assertRaises( ValidationError ):
            self.reservation.clean_fields()


    def testInvalidEmails( self ):
        addresses = ["user@foo,com", "user_at_foo.org", "example.user@foo."]
        for address in addresses:
            self.reservation.email = address
            with self.assertRaises( ValidationError ):
                self.reservation.clean_fields()


    def testValidEmails( self ):
        addresses = ["user@foo.com", "A_USER@f.b.org", "frst.lst@foo.jp", "a+b@baz.cn"]
        for address in addresses:
            self.reservation.email = address
            self.assertEqual( self.reservation.clean_fields(), None )


    def testLongEmail( self ):
        self.reservation.email = "%s@gmail.com" % ("a" * 254)
        with self.assertRaises( ValidationError ):
            self.reservation.clean_fields()


    def testInvalidPartySizes( self ):
        sizes = [-1, 50]
        for size in sizes:
            self.reservation.partySize = size
            with self.assertRaises( ValidationError ):
                self.reservation.clean_fields()


    def testValidPartySizes( self ):
        sizes = range( 1, 21 )
        for size in sizes:
            self.reservation.partySize = size
            self.assertEqual( self.reservation.clean_fields(), None )


    def testInvalidReservationDates( self ):
        dates = ["not a date"]
        for date in dates:
            self.reservation.reservationDate = date
            with self.assertRaises( ValidationError ):
                self.reservation.clean_fields()


    def testValidReservationDates( self ):
        dates = [datetime.date.today()]
        for date in dates:
            self.reservation.reservationDate = date
            self.assertEqual( self.reservation.clean_fields(), None )
