parser = argparse.ArgumentParser()
FUNCTION_SELECT = {'base64encode' : encode_base64,
                'rot13encode' : encode_rot13 }

parser.add_argument('command', choices=FUNCTION_SELECT.keys())

args = parser.parse_args()

func = FUNCTION_SELECT[args.command]
func()

sys.sleep(5)