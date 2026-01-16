from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "invites" ADD "email" VARCHAR(255) NOT NULL;
        ALTER TABLE "invites" ADD "role_id" INT NOT NULL;
        ALTER TABLE "profile" RENAME TO "profiles";
        ALTER TABLE "profiles" ADD "role_id" INT NOT NULL;
        DROP TABLE IF EXISTS "profilerole";
        ALTER TABLE "invites" ADD CONSTRAINT "fk_invites_roles_2c187d35" FOREIGN KEY ("role_id") REFERENCES "roles" ("id") ON DELETE CASCADE;
        ALTER TABLE "profiles" ADD CONSTRAINT "fk_profiles_roles_da75568c" FOREIGN KEY ("role_id") REFERENCES "roles" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "profiles" DROP CONSTRAINT IF EXISTS "fk_profiles_roles_da75568c";
        ALTER TABLE "invites" DROP CONSTRAINT IF EXISTS "fk_invites_roles_2c187d35";
        ALTER TABLE "invites" DROP COLUMN "email";
        ALTER TABLE "invites" DROP COLUMN "role_id";
        ALTER TABLE "profiles" RENAME TO "profile";
        ALTER TABLE "profiles" DROP COLUMN "role_id";"""


MODELS_STATE = (
    "eJztXWtv27gS/SuGP7WA2k3Spi2CxQKO47a+jeMgcbvdbQuDlhhbt3p49Wiau+h/v6TelC"
    "hFsiRbj1lg0VjiyNahSM05Mxz+O1R1CSvm85EoGjZShmeDf4caUjH5I35KGAzRdhueoAcs"
    "tFKctsht5BxEK9MykGiR43fkECaHJGyKhry1ZF0jRzVbUehBXSQNZW0dHrI1+R8bLy19ja"
    "0NNsiJL9/IYVmT8E9s+h+335d3MlYk5tfKEv1u5/jSetg6x6aa9dZpSL9ttRR1xVa1sPH2"
    "wdroWtBa1ix6dI01bCAL08tbhk1/Pv113p36d+T+0rCJ+xMjNhK+Q7ZiRW43JwairlH8yK"
    "8xnRtc0295dnL88vXLNy9evXxDmji/JDjy+pd7e+G9u4YOAleL4S/nPLKQ28KBMcRNNDC9"
    "2SWykvhdkDOWrGI+iKxlDEzJM33u/xGH1gcyC1v/QAhu+EBVhC65B2muKQ9ex2VAuZjOJr"
    "eL0eya3olqmv8oDkSjxYSeOXGOPsSOPnn1lB7XyXBwx0lwkcGf08X7Af04+Ht+NXEQ1E1r"
    "bTjfGLZb/D2kvwnZlr7U9PslkiLPmH/UB4a0DDvW3ko7dixrCR170I71fnzYr0jVbY3Tp6"
    "mTXWjw+IRXVecdHXrCi0xwuqpiHmDjDTJSZrbQJAYZ+aENfd5V9HOpYG1tbShUp6cZGH0a"
    "3Yzfj26ekFaxp/jKO3XinosBSW54rRsPfCQnmq06aE7J70KaiJOoRuz3B+uQ+C+2gZSx9+"
    "3PR4vF5OpidDV2xiYL9zA8eTZAloU1id7KV+16dLOYjqfXo8V0fnU22CLDkkV5i6jdV+18"
    "8n70aTq/ORus8Ab9kHXjqzYav59OPk1mk6vFLbmWuJHxD0yfKvOr9n4+m/w5v/lwNtjoKr"
    "7Xje/DHTr5+EWOPj5+kdrF9BTbw7qxXhbyo0KD/U0tTXCnQshMy5ZIpxaDjTXqK3QWJqMC"
    "G8WgY436BB1lPnffuT48GYZJCN/qBpbX2gf8kJiWY7B5RG9urJEm/8+Z05oJ4y//afCPhh"
    "6Tge4DUhiZlshdknvDlvuaGt2ORxeTIe8prAC/a0O/k5WG+sN5oWPH1+PweVNZBfDdhldq"
    "L3zszM6Hjw7kFRK/3yNDWjIjmp7RT/TYkaBt8pR6osaPIA2tHQjojdCf7cs4gTcz5Ik84V"
    "khU+cJ2oHUA1IPKAIg9UDH1if13CNzuSVX475gz3VdwUjj92vMMtaxK2JaV18WfQ/wX7S8"
    "zjufzy+ZfjufLmLc9uPsfEI4r9NhpJHsvnkLaEIL/DPlPVJWE/K6e/8+C3ccTD4vGCh9Ve"
    "DJbPT5KTMMLudX7/zmEaTHl/PzGKgKNk0CS6G3M2PTJzYHsgvILqAdNJDBFdEO3NmrAvgu"
    "gwu1FzhmKgfhoDPCwVhBpmnoujrk6AbhSSFLNhCZZiAaNOz1IIBo0HVuCaJBRzs2IRpYsu"
    "UGIfJmOwQG7cx1OD46yhMHPzpKD4TTcyy/uFN0nRMTSn1hBO13YhX71waq5mMrW1Yk+oUF"
    "nruoTUsklT08eSAGAKPdL6NNpxVxpmtyVGjP8O2HG6wEYJVkuQfTShNYMkNziw1Zl5aVYH"
    "HtXKuNiNTJNS8wzaxzdHYO2YycFbLYpsS2A7rZsLlbALrZdVYCdLOjHZt4KTr/FvD6/fZA"
    "NiPRaIkDYerbwm/eJ3cfGBIwpGYzJKxuFf0B45K8YOJdBjhBAhEOI4iilc4HcLQVsIGGzV"
    "PABjrvNAIb6GjHAhuong2YtlEUxYgJABnKtcgydO1BlcUiWLJWEJcK/VskK0WADAxaiWEt"
    "K+hDYboYgU3Y9TTKDMx/J8hUrK6KrrNO2PUJQJBOakmXZuNyJSFkg4GNm/ry4peY2h+HMR"
    "yaFT+Js+Ci7X4emXlrd0UvtTJAET1vEV6kPaDWque9M5DEFfPcE0KWkremTWDlOeh4IPeA"
    "jgcdW5+O9wMpdpGYdNB+b8y0DRUGYTX57qvJnVf9ko5//szCx5W1yppV2gYynRRgwT3oSA"
    "eCDBbcg4J0eAUJFtzDgvvOL7ifaj/cwkUJhcQ7I2RJJLLTBjQS0EiASoNGAh1bn0ZCXpOW"
    "zUn3zcjTCSzamaZzmiev5DQ9reT00FklB0ewlrQSoLOF6ezWrdVdDDbWqK/QGXpR3CIWfQ"
    "INNIBaNAD6NFUA3o3e9lL9kWH1OGrbcHOCksB1YpsDdipvEvv3lCkO+w81q3T2HwpkQP6b"
    "9j4QgPx3nSMC+e9ox/a+yt5JrjUlJxlrSk44S50sZFhL//GN5U6kDgzWKm1g5BwUlcX4h9"
    "cKRiYe2OR/8tYc3OmKot8TgMlfhoqss8HvWP3jL/Lfs9ns2cXF77+Rj8+HRbyatGHDjA3u"
    "uAh74c1T3ligw4DVZTSpcL9EbaBX6uiVotkwFeXBHM6Pz5kIc4/x96WEODuTpvqeUZM+iR"
    "JR2GRzKVKup2CO1565vUzMEraXSQKrq1vKKHdBNmoK0MamQNsI9K7ki+nCO5syHUZs+zrm"
    "D7Ab9sGX8tbhugY7GhSTwuNmsJAXIlbFEjDXhm5vd0vDjJr29MEz7dV/sVg0jZUx6ilyh9"
    "qtu53IQeyv4Zt151+X29y140X36mZ2YSqJH7PxU2sRjLtjDIa3k8Xg6uPlJTeN2n2ZVgCk"
    "l0z9zr9ca7HkeRk5stLdd2sVQIZXai+GjKexe+mCyDbtJeuRshvDt+ctk1xLWBKIoDpBiz"
    "CoM0+BcUA42QpxByU9Z0GPt4TMhYZ5swJkLnQ9wA2ZCx3t2MZlLtQ+4dWTcJ9g9Ln8MFE0"
    "bAJAWSfMvUwzR0ouDwwcUj4TLwlGERbeVCzCCnglwShUEbCpaOx/G4mmIuGSth6yNiaTwF"
    "3NXRKFcN14S2HY7/aTTUUhSpS9IpclIWl79U92icvhtudsKiSeJlt2/mhlwY901b4aNPIq"
    "9q2AxJ9OKoSm9fOJJ8aXhSR3WKKpOHhhxpI4QCHkLAXdGyyP6OjhkMqnpkfKhIOoDqI6aK"
    "8gqkPH1iKqQ0Ir1BHZB2i2iY3lTsVrOJaQj+mNxAqyj/qZjxl9qCoAMX9pkeamcHHGGdS0"
    "qa6mTZ6oa3S/516HUFJL/nZf/KuTuDPiMIeyx8XjdLLOSNZA04GmA5sDmg4d29nctz30HV"
    "Tt6W99GKja08RecZ28ZJ/cqkhR0osNB1btkmlenLx+FfhZ9EOWi3U7G11ecqRBvCXukZ/J"
    "sbQ1S1YKbwWWeZGO7wzmTrZFEWOtOg4RFPCAAh5QwKN9KEIBDyjgAQGjJmn2UMADCngcCk"
    "Eo4AEFPBqFYakCHjUHrVTZNFOqNUTOCo8ErLx2sMMkhKsgqgHhKujY+sJVoi4Vilb57dtY"
    "qOE4V6jqOCNUdZwMVTn/FgDQb9/SaN9Ba104qVsx/2D3rCOaysY6Jc1D/zDJR16OJM+JC9"
    "MnMzw4txG4b+C+wVse3Dfo2PrcNycVvPgijX6HycBl28llYyU5oyiKERMAMszcQdbG0Mkn"
    "WSwCZswMAIU1fxWGH2GtUJVrhfwKjeXYavsLNHqFxsrB0Po6Yw2psNWc+FatUoYzBXF0DH"
    "9qShcx6NAHBQMUDCC6oGBAx0IAqgrCc5on/nSaHn46TUSf+rbarLIQ3k7xJyiV694HXqnY"
    "WPJZYn9rw3pRr7JlYXMXKGkqEBCl3Ru1yc64S0KXTXfinVYt8/kSyErh1wy/AR8CPgRuM/"
    "ChvnYsr8S8NzkWi2Ik7PoUy4AA0A6gZQSAtozXUDIM1FbvTYgFgxIjDIru7SOQVqcP7Ree"
    "4zjPkZp06V6zv/kFxAnALwb3Cfxi6Nja/OJ+Je3VslSlj0l7tQC5NXT6YHOUzQssyipSUi"
    "haxCw+vbh2zz37upA9Ku3p8VC8mIyns9Hlk1PhxEGRTBqy6975+L5MQLiSDWsjoQf+JM3H"
    "L2pTsnTU4VxlLoCc8loiIQkFXLug/f4YbImHCWpFNQIyN/2sOHKMXZ8AzJBMoGTP7iV7wm"
    "eqYgjbGFTmAckMOMhEhq3iK4XD3Qa7HBBt3wWb2aJ0I1e5gWsbJ6FaMxeYclbp0mtQ7upR"
    "/TUstAUibNNcJgFE2K5rdSDCdrRjYXOLOlaoglgBXHu/XDsPN/Q2MSjn9oYbkrVn+WFyH4"
    "1lJVjEt2hrJyKVrFAFNpSTDXngPMKJQghzMqPoOmNgSE170QnAkLruSAND6mjHpuiIhaa7"
    "0luutNTBB05UyWY/O23z0z/ogE7WErpN3f97100u2g0dO74eh+9AO4Q0GMHHtwY50FIBb+"
    "sQHjcLdxXJIGSRRkDBGvZyEICCdd1TBwrW0Y7tfZCqlhR3go7OycbLqsvkGbQTxKx3hA/h"
    "61QAX0OMD0gZxPiENkS0IMZXd0TL3zeVQ5UiW6qmU6XIDq5AlZo2ZQtAlbruUQNV6mjHJt"
    "6FWN0q+gMuWC8nZtUnhxV8fPDxmxF48QdhBQBOIpdqL3ixWQlYErCkRrOkEUFF3Aw5JMk7"
    "I2RxJBS2AYrUsDeekEGRfmCDX1YvXVmNmLRTW61lFQUdGgVA9Jq3E8CaFH7N4mZu/Od2fp"
    "Wm8QcmMSA/auQGv0iyaAkDRTatb82ENQNFetcMafPBezIbfY7jOr6cn8fZGL3AebGdBap/"
    "vfz6P1fEP6I="
)
