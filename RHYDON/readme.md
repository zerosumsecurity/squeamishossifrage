## RHYDON

We discovered a vague prime generation routine, containing obscure references to the Collatz conjecture. 

Also, we have a bunch of certificates which were build using these kind of primes. In order to recover the flag, you will need to find the corresponding private key to at least one of these certificates.

The underlying waek prime class has a.o. been used in the 2017 online challenge bij the AIVD, the Dutch intelligence and security service. In this case a <a href='https://twitter.com/falken_dr'>number station</a> tweeted out a flag and coordinates, encrypted with this certificate:

    -----BEGIN CERTIFICATE-----
    MIIC1DCCAnmgAwIBAgIDHoy9MA0GCSqGSIb3DQEBCwUAMIHDMQswCQYDVQQGEwJO
    TDEVMBMGA1UECAwMWnVpZC1Ib2xsYW5kMRMwEQYDVQQHDApab2V0ZXJtZWVyMRcw
    FQYDVQQKDA5OdW1iZXIgU3RhdGlvbjElMCMGA1UECwwcQSBuZXcgY2xhc3Mgb2Yg
    dW5zYWZlIHByaW1lczEXMBUGA1UEAwwOU3RlcGhlbiBGYWxrZW4xLzAtBgkqhkiG
    9w0BCQEWIGRyLnN0ZXBoZW4uZmFsa2VuQHByb3Rvbm1haWwuY29tMB4XDTE3MTEw
    OTExMzMzOFoXDTE4MTEwOTExMzMzOFowgcMxCzAJBgNVBAYTAk5MMRUwEwYDVQQI
    DAxadWlkLUhvbGxhbmQxEzARBgNVBAcMClpvZXRlcm1lZXIxFzAVBgNVBAoMDk51
    bWJlciBTdGF0aW9uMSUwIwYDVQQLDBxBIG5ldyBjbGFzcyBvZiB1bnNhZmUgcHJp
    bWVzMRcwFQYDVQQDDA5TdGVwaGVuIEZhbGtlbjEvMC0GCSqGSIb3DQEJARYgZHIu
    c3RlcGhlbi5mYWxrZW5AcHJvdG9ubWFpbC5jb20wYDANBgkqhkiG9w0BAQEFAANP
    ADBMAkURXYR60ACHfcS7z3cpAasKnxzfNHL0sFyBSEgsNlPiAr7PhOMzQWwv378j
    UvAG4hCzAHk/5bCy+p/KizWN0P76mPXyjXUCAwEAAaNQME4wHQYDVR0OBBYEFARO
    9fnH8imSIY05p0uuwoA/uoa6MB8GA1UdIwQYMBaAFARO9fnH8imSIY05p0uuwoA/
    uoa6MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADRgAOikMR/uE9L1R+PPHF
    //4MSERTssn0Dli81gr2YycahEsiJccIkaJjNOn+OWa8DuuAL/vJBuMeFb5lCjK6
    KORZweHaDfw=
    -----END CERTIFICATE-----


Flag is of the form so{<32 hexadecimal charachters>}. Submit your flag at the Squeamish Ossifrage <a href='https://squeamishossifrage.eu'>website</a>.