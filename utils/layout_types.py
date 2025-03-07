import os

script_path = os.path.expanduser('~/Documents/python/wp-python/')
layout_types = (
        {
            'type': 'php',
            'dir_name': 'template-parts',
            'layout_text': 'home',
            'create_file_input_placeholder': 'home',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-layout.php',
            'create_dir': True
            },
        {
            'type': 'scss',
            'dir_name': 'src/scss/blocks',
            'layout_text': 'home',
            'create_file_input_placeholder': 'home',
            'extension': 'scss',
            'layout_path': f'{script_path}layouts/scss-layout.scss',
            'create_dir': True
            },
        {
            'type': 'phpc',
            'dir_name': 'components',
            'layout_text': 'defaultComponent',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-component.php',
            'create_dir': False
            },
        {
            'type': 'phpp',
            'dir_name': '',
            'layout_text': 'phpPageLayout',
            'create_file_input_placeholder': 'page-servizi',
            'extension': 'php',
            'layout_path': f'{script_path}layouts/php-page.php',
            'create_dir': False
            },
        {
            'type': 'phpi',
            'dir_name': 'template-parts/icons',
            'layout_text': 'phpIcon',
            'create_file_input_placeholder': 'facebook',
            'extension': 'php',
            'layout_path': '',
            'create_dir': False
            },
        {
            'type': 'js',
            'dir_name': 'src/js/modules',
            'layout_text': 'jsLayout',
            'create_file_input_placeholder': 'homeIntro',
            'extension': 'ts',
            'layout_path': f'{script_path}layouts/js_layout.ts',
            'create_dir': True
            },
        {
            'type': 'ts',
            'dir_name': 'src/vue/interfaces',
            'layout_text': 'IDefault',
            'create_file_input_placeholder': 'IProduct',
            'extension': 'ts',
            'layout_path': f'{script_path}layouts/interface.ts',
            'create_dir': False
            },
        {
            'type': 'type',
            'dir_name': 'src/vue/types',
            'layout_text': 'TDefault',
            'create_file_input_placeholder': 'TProduct',
            'extension': 'ts',
            'layout_path': f'{script_path}layouts/type.ts',
            'create_dir': False
            },
        {
            'type': 'vue_view',
            'dir_name': 'src/vue/views',
            'layout_text': 'vue',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'vue',
            'layout_path': f'{script_path}layouts/vue-component.vue',
            'create_dir': False
            },
        {
            'type': 'vue',
            'dir_name': 'src/vue/components',
            'layout_text': 'vue',
            'create_file_input_placeholder': 'myComponent',
            'extension': 'vue',
            'layout_path': f'{script_path}layouts/vue-component.vue',
            'create_dir': True
            },
        {
                'type': 'hook',
                'dir_name': 'src/vue/hooks',
                'layout_text': 'useDefault',
                'create_file_input_placeholder': 'useDefault',
                'extension': 'ts',
                'layout_path': f'{script_path}layouts/default-hook.ts',
                'create_dir': False
                },
        {
                'type': 'pinia',
                'dir_name': 'src/vue/pinia',
                'layout_text': 'useDefault',
                'create_file_input_placeholder': 'default',
                'extension': 'ts',
                'layout_path': f'{script_path}layouts/default-pinia.ts',
                'create_dir': False
                },
        )

