import os
import subprocess
import unittest


class TestHelloWorldBundle(unittest.TestCase):
    def test_hello_world(self):
        result = self.run_batect('say-hello')

        self.assertIn('\nHello world!\n', result.stdout)

    def run_batect(self, task):
        command = ['./batect', '-f=batect-bundle.yml', '--output=quiet', task]

        env = {
            **os.environ,
            'BATECT_QUIET_DOWNLOAD': 'true',
        }

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        if result.returncode != 0:
            raise AssertionError('Command failed with exit code ' + str(result.returncode) + ' and output: \n' + result.stdout)

        return result


if __name__ == '__main__':
    unittest.main()
