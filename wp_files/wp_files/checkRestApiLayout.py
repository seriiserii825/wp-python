import os

from termcolor import colored


def checkRestApiLayout(layout_path):
    if not os.path.exists(layout_path):
        print(colored("Creating rest-api layout file...", "green"))
        with open(layout_path, "w") as f:
            layout_code = """
<?php
if (!defined('ABSPATH')) {
  exit; // Exit if accessed directly
}
function eventsApi()
{
  register_rest_route('events/v1', 'page', [
    'methods' => WP_REST_SERVER::READABLE,
    'callback' => 'eventsApiFunc',
  ]);
}

add_action('rest_api_init', 'eventsApi');
function eventsApiFunc()
{
  return [
      'result' => 'success',
  ];
}
            """
            f.write(layout_code)
    else:
        print(colored("Layout rest-api exists", "blue"))
