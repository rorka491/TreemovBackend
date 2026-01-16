from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "emailcode" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL,
    "code" VARCHAR(255) NOT NULL,
    "purpose" VARCHAR(50) NOT NULL,
    "is_used" BOOL NOT NULL DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expires_at" TIMESTAMPTZ NOT NULL
);
COMMENT ON COLUMN "emailcode"."purpose" IS 'login: login\nverify_email: verify_email\nreset_password: reset_password';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "emailcode";"""


MODELS_STATE = (
    "eJztl21P2zAQx79KlFedxBB0FFDftaUTnWg7QdgmHhS5iZtaOHaIHaBCfPf5nOekqQraBJ"
    "V41eTuf8nd71z78mz63MVU7A59ROhAXZtd49lkyIeLunPHMFEQ5C4wSDSjWo1B5qSymZAh"
    "cqRyzBEVWJlcLJyQBJJwpqwsohSM3FFCwrzcFDFyH2Fbcg/LBQ6V4/pWmQlz8RMW6W1wZ8"
    "8Jpm4pYeLCu7XdlstA20ZMftdCeNvMdjiNfJaLg6VccJapCZNg9TDDIZIYHi/DCNKH7JJS"
    "04riTHNJnGIhxsVzFFFZKHdDBg5nwE9lI3SBHrzla3v/4Ojg+NvhwbGS6Ewyy9FLXF5eex"
    "yoCUws80X7kUSxQmPMuenW1dENFihczS4LqOBTSVfxpbDW8UsNOcB80fwjgj56silmnlwA"
    "tk5nDa9fvfPBae+8pVRfoBquFnK8xCeJqx37AGoOMV36mzJM9Z8IM4RBFAZcNFAcssjXJE"
    "cqLcQcXCNaCH9nqCblHmFdQ//csAcckvnS1v+arlG8u2EhFljaARLikYdu1yjfm29oTWdv"
    "g8509hobA65yX4iwI4FXbK59zilGrGGDzaMq7ZipsP/Vj9ceNxWUa9D1p9MzyNoX4p5qw8"
    "iqMLwc94fnrX2NVomIxMUNuLBXhBjKtpGsMz1RHkl83LBrlCIrXN0kdDe9+KA7iarBnTK6"
    "TE7KNcyt0Xh4YfXGP0vgT3rWEDxtbV1WrK3DytLOHmL8HlmnBtwaV9PJUBPkQnqhfmOus6"
    "5MyAlFktuMP9rILRzqqTUFU2osfgqIetobGluO3M7Gbkkj07JrnYTBcn5XGJHAMEPO3SMK"
    "Xbvm4W3epK27/LZftSCGPN0HoAl5JgN3Tx0QzsJcMYonnrVzOMo1n0P4Fg3haiwQkNIrRs"
    "hCyOcUmYGEv8YrICby7QS4v7fJsKdUjQC1r/olwyRmK06wHxfTSdPHTBZSAXnJVIHXLnHk"
    "jkGJkLcfE+sailB16dRK4bXGvT9VroOzab96HMED+orxux4vL38Bd/q7ZA=="
)
