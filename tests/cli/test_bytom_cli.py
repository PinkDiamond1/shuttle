#!/usr/bin/env python3
# coding=utf-8

from shuttle.cli import __main__ as cli_main


RAW = "eyJmZWUiOiAxMDAwMDAwMCwgImd1aWQiOiAiZjBlZDZkZGQtOWQ2Yi00OWZkLTg4NjYtYTUyZDEwODNhMTNiIiwgInVuc2lnbmVkIjogW3s" \
      "iZGF0YXMiOiBbIjg0MGYwZjM5MTFiOTllY2NlODk0MjA0OWFhYjY4NjEzMmE5MTAzNTBiZTAxNDY0MTU1YzkzM2ZjMWE5Y2NmZjQiXSwgIm" \
      "5ldHdvcmsiOiAibWFpbm5ldCIsICJwYXRoIjogbnVsbH0sIHsiZGF0YXMiOiBbIjg2ZGFiNjAwZWFjMDMxYjM4YjE2YmQ1NGQzMjMwYjgyN" \
      "WUwYjI2YmNkZGZkZGJhNTdjODBhZDNmNjI4YTllYTIiXSwgInB1YmxpY19rZXkiOiAiOTFmZjdmNTI1ZmY0MDg3NGM0ZjQ3ZjBjYWI0MmU0" \
      "NmUzYmY1M2FkYWQ1OWFkZWY5NTU4YWQxYjY0NDhmMjJlMiIsICJuZXR3b3JrIjogIm1haW5uZXQiLCAicGF0aCI6ICJtLzQ0LzE1My8xLzA" \
      "vMSJ9XSwgImhhc2giOiAiZTg5OWVjNzlhN2IxYTk0MzFjYjczNWMxYmMxYmNhYzg1MDJjZjZkYmY3NTA0ODdjMzcxYjQ0NDFkNTUyNmVjNi" \
      "IsICJyYXciOiAiMDcwMTAwMDIwMWQwMDEwMWNkMDEzZmJmMjRiNDBjOWE3OGI1Zjc2YmVlNWU2YjI0MjhhOWVjNThhYmQ2NDA0OTVkNDk4N" \
      "DQwOTYyNDFhMmMwMzY1ZjM3ZGVhNjJlZmQyOTY1MTc0Yjg0YmJiNTlhMGJkMGE2NzFjZjVmYjI4NTczMDNmZmQ3N2MxYjQ4MmI4NGJkZjY0" \
      "MDAwMTg4MDEwMTY0MjA5MWZmN2Y1MjVmZjQwODc0YzRmNDdmMGNhYjQyZTQ2ZTNiZjUzYWRhZDU5YWRlZjk1NThhZDFiNjQ0OGYyMmUyMjB" \
      "hYzEzYzBiYjE0NDU0MjNhNjQxNzU0MTgyZDUzZjA2NzdjZDQzNTFhMGU3NDNlNmYxMGIzNTEyMmMzZDdlYTAxMjAyYjlhNTk0OWY1NTQ2Zj" \
      "YzYTI1M2U0MWNkYTZiZmZkZWRiNTI3Mjg4YTdlMjRlZDk1M2Y1YzI2ODBjNzBkNmZmNzQxZjU0N2E2NDE2MDAwMDAwNTU3YWE4ODg1MzdhN" \
      "2NhZTdjYWM2MzFmMDAwMDAwNTM3YWNkOWY2OTcyYWU3Y2FjMDBjMDAxMDAwMTYwMDE1ZTNmYmYyNGI0MGM5YTc4YjVmNzZiZWU1ZTZiMjQy" \
      "OGE5ZWM1OGFiZDY0MDQ5NWQ0OTg0NDA5NjI0MWEyYzAzNjVmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZ" \
      "mZmZmZmZmZmZmZmZmZmZmZmZmODBkZDk2ZmQwODAxMDExNjAwMTQyY2RhNGY5OWVhODExMmU2ZmE2MWNkZDI2MTU3ZWQ2ZGM0MDgzMzJhMj" \
      "IwMTIwOTFmZjdmNTI1ZmY0MDg3NGM0ZjQ3ZjBjYWI0MmU0NmUzYmY1M2FkYWQ1OWFkZWY5NTU4YWQxYjY0NDhmMjJlMjAyMDEzOWYzN2RlY" \
      "TYyZWZkMjk2NTE3NGI4NGJiYjU5YTBiZDBhNjcxY2Y1ZmIyODU3MzAzZmZkNzdjMWI0ODJiODRiZGY2NDAxMTYwMDE0MTFiYzE5MGY0ZWJl" \
      "M2E2ZGRjYmM3YWVmNjk3M2FjNGE4OTNiNDQ1NjAwMDEzZGZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZ" \
      "mZmZmZmZmZmZmZmZmZmZmZmY4MGIwYjRmODA4MDExNjAwMTQyY2RhNGY5OWVhODExMmU2ZmE2MWNkZDI2MTU3ZWQ2ZGM0MDgzMzJhMDAiLC" \
      "Aic2VjcmV0IjogIkhlbGxvIE1laGVyZXQhIiwgIm5ldHdvcmsiOiAibWFpbm5ldCIsICJzaWduYXR1cmVzIjogW10sICJ0eXBlIjogImJ5d" \
      "G9tX2NsYWltX3Vuc2lnbmVkIn0="

XPRIVATE_KEY = "205b15f70e253399da90b127b074ea02904594be9d54678207872ec1ba31ee51ef4490504bd2b6f997113671892458830d" \
               "e09518e6bd5958d5d5dd97624cfa4b"

SIGNED = "eyJmZWUiOiAxMDAwMDAwMCwgImd1aWQiOiAiZjBlZDZkZGQtOWQ2Yi00OWZkLTg4NjYtYTUyZDEwODNhMTNiIiwgInJhdyI6ICIwNzAx" \
         "MDAwMjAxZDAwMTAxY2QwMTNmYmYyNGI0MGM5YTc4YjVmNzZiZWU1ZTZiMjQyOGE5ZWM1OGFiZDY0MDQ5NWQ0OTg0NDA5NjI0MWEyYzAz" \
         "NjVmMzdkZWE2MmVmZDI5NjUxNzRiODRiYmI1OWEwYmQwYTY3MWNmNWZiMjg1NzMwM2ZmZDc3YzFiNDgyYjg0YmRmNjQwMDAxODgwMTAx" \
         "NjQyMDkxZmY3ZjUyNWZmNDA4NzRjNGY0N2YwY2FiNDJlNDZlM2JmNTNhZGFkNTlhZGVmOTU1OGFkMWI2NDQ4ZjIyZTIyMGFjMTNjMGJi" \
         "MTQ0NTQyM2E2NDE3NTQxODJkNTNmMDY3N2NkNDM1MWEwZTc0M2U2ZjEwYjM1MTIyYzNkN2VhMDEyMDJiOWE1OTQ5ZjU1NDZmNjNhMjUz" \
         "ZTQxY2RhNmJmZmRlZGI1MjcyODhhN2UyNGVkOTUzZjVjMjY4MGM3MGQ2ZmY3NDFmNTQ3YTY0MTYwMDAwMDA1NTdhYTg4ODUzN2E3Y2Fl" \
         "N2NhYzYzMWYwMDAwMDA1MzdhY2Q5ZjY5NzJhZTdjYWMwMGMwMDEwMDAxNjAwMTVlM2ZiZjI0YjQwYzlhNzhiNWY3NmJlZTVlNmIyNDI4" \
         "YTllYzU4YWJkNjQwNDk1ZDQ5ODQ0MDk2MjQxYTJjMDM2NWZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZm" \
         "ZmZmZmZmZmZmZmZmZmZmZmZmZmY4MGRkOTZmZDA4MDEwMTE2MDAxNDJjZGE0Zjk5ZWE4MTEyZTZmYTYxY2RkMjYxNTdlZDZkYzQwODMz" \
         "MmEyMjAxMjA5MWZmN2Y1MjVmZjQwODc0YzRmNDdmMGNhYjQyZTQ2ZTNiZjUzYWRhZDU5YWRlZjk1NThhZDFiNjQ0OGYyMmUyMDIwMTM5" \
         "ZjM3ZGVhNjJlZmQyOTY1MTc0Yjg0YmJiNTlhMGJkMGE2NzFjZjVmYjI4NTczMDNmZmQ3N2MxYjQ4MmI4NGJkZjY0MDExNjAwMTQxMWJj" \
         "MTkwZjRlYmUzYTZkZGNiYzdhZWY2OTczYWM0YTg5M2I0NDU2MDAwMTNkZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZm" \
         "ZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZjgwYjBiNGY4MDgwMTE2MDAxNDJjZGE0Zjk5ZWE4MTEyZTZmYTYxY2RkMjYxNTdlZDZk" \
         "YzQwODMzMmEwMCIsICJoYXNoIjogImU4OTllYzc5YTdiMWE5NDMxY2I3MzVjMWJjMWJjYWM4NTAyY2Y2ZGJmNzUwNDg3YzM3MWI0NDQx" \
         "ZDU1MjZlYzYiLCAidW5zaWduZWQiOiBbeyJkYXRhcyI6IFsiODQwZjBmMzkxMWI5OWVjY2U4OTQyMDQ5YWFiNjg2MTMyYTkxMDM1MGJl" \
         "MDE0NjQxNTVjOTMzZmMxYTljY2ZmNCJdLCAibmV0d29yayI6ICJtYWlubmV0IiwgInBhdGgiOiBudWxsfSwgeyJkYXRhcyI6IFsiODZk" \
         "YWI2MDBlYWMwMzFiMzhiMTZiZDU0ZDMyMzBiODI1ZTBiMjZiY2RkZmRkYmE1N2M4MGFkM2Y2MjhhOWVhMiJdLCAicHVibGljX2tleSI6" \
         "ICI5MWZmN2Y1MjVmZjQwODc0YzRmNDdmMGNhYjQyZTQ2ZTNiZjUzYWRhZDU5YWRlZjk1NThhZDFiNjQ0OGYyMmUyIiwgIm5ldHdvcmsi" \
         "OiAibWFpbm5ldCIsICJwYXRoIjogIm0vNDQvMTUzLzEvMC8xIn1dLCAibmV0d29yayI6ICJtYWlubmV0IiwgInNpZ25hdHVyZXMiOiBb" \
         "WyI0ODY1NmM2YzZmMjA0ZDY1Njg2NTcyNjU3NDIxIiwgIjdjNjA5OWY1MTIzYWIwZThjZTgzYWZmNDVmZTgxMWVmNmI0OTBjNjg3YWU3" \
         "ZWQ0NTc5ZDQ3NDhjMzk2ZjM5MGNjMDE4Mzk5NjRmYTU2MmFhMzg0M2IwMDBhYzIzOTcxZjEzNWJiMDczMDBiMDI2YjQ1OTdjNWMyNGNj" \
         "ZGJiNDA5IiwgIiJdLCBbIjRiYTFiZDA5NjYyMmJiNjdjMmU3MGI0ZDlmZDhhOWU5MmNiMjk5YjM4MDRlZTQzNzNhMzU3Y2FhMjNkNWMz" \
         "NDQ5MzJjNjM4ZmU4OGM4MDA3NDEzNTMyYWRjMjgyZWVkYzQyNjg2NjZiMDg3ODk2ZWExYWFjNTFlNWNhODQyODA3Il1dLCAidHlwZSI6" \
         "ICJieXRvbV9jbGFpbV9zaWduZWQifQ=="


# Success template
def success(_):
    return "[{}] {}".format("SUCCESS", str(_))


def test_bytom_cli(cli_tester):
    assert cli_tester.invoke(cli_main.shuttle,
                             ["bytom"]).exit_code == 0

    # Testing bytom decode command.
    decode = cli_tester.invoke(cli_main.shuttle,
                               ["bytom", "decode", "--raw", RAW])
    assert decode.exit_code == 0
    assert decode.output != success("") + "\n"

    # Testing bytom sign command.
    sign = cli_tester.invoke(cli_main.shuttle,
                             ["bytom", "sign", "--unsigned", RAW, "--xprivate", XPRIVATE_KEY])
    assert sign.exit_code == 0
    assert sign.output == success(SIGNED) + "\n"

    # Testing bytom submit command.
    submit = cli_tester.invoke(cli_main.shuttle,
                               ["bytom", "submit", "--raw", RAW])
    assert submit.exit_code == 0
    assert submit.output == "[ERROR] finalize tx fail" + "\n"
