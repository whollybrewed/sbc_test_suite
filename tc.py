import utility as util
import singlestage
import twostage

def test_bad_meta_data(bl):
    # test booting to an image with bad metadata
    assert util.is_failed()
    return


def test_corrupted_image(bl):
    # test booting to a currupt
    bl.use_image()
    assert util.is_failed()
    return


def test_inauthentic_image(bl):
    # test booting to a inauthentic image
    bl.use_image()
    assert util.is_failed()
    return

def test_upgrade_bad_bootloader(bl):
    # test flashing a bad 2nd-stage bootloader
    bl.use_image()
    assert util.is_failed()
    return
