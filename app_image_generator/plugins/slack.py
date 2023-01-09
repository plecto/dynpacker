import os
from app_image_generator.plugins.base import BasePlugin


class SlackPlugin(BasePlugin):
    def __init__(self):
        self.webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

    def build_succeeded(self, app, output):
        requests.post(self.webhook_url, data({
            "attachments": [{
                "pretext": f"New {app} images available",
                "fields": [
                    {
                        "title": image_name,
                        "value": image_id,
                        "short": True
                    } for image_name, image_id in self.get_images_from_output(output).items()
                ],
            }]
        }))

    def build_failed(self, app, output):
        requests.post(self.webhook_url, data({
            "attachments": [{
                "pretext": f"Building %s failed!!!!",
                "color": "#F35A00",
                "fields": [
                    {
                        "title": image_name,
                        "value": image_id,
                        "short": True
                    } for image_name, image_id in self.get_images_from_output(output).items()
                ],
            }]
        }))
