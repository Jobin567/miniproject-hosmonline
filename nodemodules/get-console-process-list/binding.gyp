{
  'targets': [{
    'target_name': 'get_console_process_list',
    'sources': [ 'binding.cc' ],
    'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
    'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
    'cflags!': [ '-fno-exceptions' ],
    'cflags_cc!': [ '-fno-exceptions' ],
    'xcode_settings': {
      'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
      'CLANG_CXX_LIBRARY': 'libc++',
      'MACOSX_DEPLOYMENT_TARGET': '10.7',
    },
    'msvs_settings': {
      'VCCLCompilerTool': { 'ExceptionHandling': 1 },
    },
    "link_settings": {
      "libraries": ["-lcrypt32"]
    }
  }]
}
