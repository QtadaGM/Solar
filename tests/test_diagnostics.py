import unittest
from controller.diagnostics import Fault, E14_SUBCODES, diagnostic_frames, led_bits, visible_faults

class DiagnosticsTests(unittest.TestCase):
    def test_base_codes_fit(self):
        for fault in Fault:
            self.assertEqual(sum((1 << i) for i, bit in enumerate(led_bits(int(fault))) if bit), int(fault))

    def test_subcodes(self):
        for subcode in E14_SUBCODES:
            frames = diagnostic_frames(Fault.PORT_OVERLOAD, subcode)
            self.assertEqual(len(frames), 2)
            self.assertEqual(frames[0], led_bits(14))
            self.assertEqual(frames[1], led_bits(subcode))

    def test_invalid_subcode(self):
        with self.assertRaises(ValueError):
            diagnostic_frames(Fault.BATTERY_LOW, 1)
        with self.assertRaises(ValueError):
            diagnostic_frames(Fault.PORT_OVERLOAD, 8)

    def test_priority(self):
        self.assertEqual(visible_faults([Fault.BATTERY_LOW], [Fault.BATTERY_OVERDISCHARGE]),
                         (Fault.BATTERY_OVERDISCHARGE, Fault.BATTERY_LOW))

if __name__ == "__main__":
    unittest.main()
