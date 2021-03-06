from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices that the table is nicely centered
        table = self.browser.find_element_by_id("exercises")
        self.assertAlmostEqual(
            table.location["x"] + table.size["width"] / 2, 512, delta=10
        )

        # She visits the first exercise and sees that the description is
        # centered.
        link = self.get_exercise_link(1)
        self.browser.get(link)
        description = self.get_description()
        self.assertAlmostEqual(
            description.location["x"] + description.size["width"] / 2, 512, delta=10
        )

        # She also notices that it is rendered as nice markdown.
        # centered.
